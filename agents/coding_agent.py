import os

from agents.planning_agent import (
    PlanningAgent
)

from agents.file_generation_agent import (
    FileGenerationAgent
)

from agents.debug_agent import (
    DebugAgent
)

from tools.project_tool import (
    ProjectTool
)

from models.project_state import (
    ProjectState
)

from core.project_context import (
    ProjectContext
)

from core.logger import (
    HelixLogger
)

from core.event_bus import (
    EventBus
)

from core.config import (
    WORKSPACE_PATH
)


class CodingAgent:

    logger = HelixLogger(
        "coding"
    )

    @staticmethod
    def emit(message):

        EventBus.emit({
            "type": "agent_step",
            "agent": "coding_agent",
            "message": message
        })

        CodingAgent.logger.log(
            message
        )

    @staticmethod
    def execute(prompt):

        CodingAgent.emit(
            "Creating project plan..."
        )

        plan = (
            PlanningAgent.create_plan(
                prompt
            )
        )

        state = ProjectState(
            plan["project_name"],
            plan["project_type"],
            plan["run_command"]
        )

        project_context = (
            ProjectContext()
        )

        project_path = (
            ProjectTool.create_project(
                WORKSPACE_PATH,
                plan["project_name"]
            )
        )

        CodingAgent.emit(
            f"Project created at {project_path}"
        )

        ProjectTool.create_folder_structure(
            project_path,
            plan["files"]
        )

        generated_files = {}

        for file in plan["files"]:

            CodingAgent.emit(
                f"Generating {file['path']}..."
            )

            context_prompt = (
                project_context.build_context_prompt()
            )

            code = (
                FileGenerationAgent.generate_file(
                    project_prompt=prompt,
                    project_plan=plan,
                    current_file=file,
                    existing_files=context_prompt
                )
            )

            full_path = os.path.join(
                project_path,
                file["path"]
            )

            with open(
                full_path,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(code)

            generated_files[
                file["path"]
            ] = code

            project_context.add_file(
                file["path"],
                code
            )

            state.generated_files.append(
                file["path"]
            )

        CodingAgent.emit(
            "Installing dependencies..."
        )

        ProjectTool.install_dependencies(
            project_path,
            plan.get(
                "dependencies",
                []
            )
        )

        ProjectTool.create_requirements_file(
            project_path,
            plan.get(
                "dependencies",
                []
            )
        )

        CodingAgent.emit(
            "Executing project..."
        )

        execution = (
            ProjectTool.run_project(
                project_path,
                plan["run_command"]
            )
        )

        retry_count = 0

        while (
            not execution["success"]
            and retry_count < 3
        ):

            CodingAgent.emit(
                "Execution failed. Starting autonomous debugging..."
            )

            debug_result = (
                DebugAgent.analyze_error(
                    prompt,
                    plan,
                    generated_files,
                    execution["stderr"] + execution["stdout"]
                )
            )

            broken_file = (
                debug_result[
                    "broken_file"
                ]
            )

            CodingAgent.emit(
                f"Repairing {broken_file}..."
            )

            fixed_code = (
                DebugAgent.fix_file(
                    project_prompt=prompt,
                    broken_file_path=broken_file,
                    broken_file_code=generated_files[
                        broken_file
                    ],
                    error_output=execution[
                        "stderr"
                    ] + execution["stdout"],
                    fix_strategy=debug_result[
                        "fix_strategy"
                    ]
                )
            )

            broken_path = os.path.join(
                project_path,
                broken_file
            )

            with open(
                broken_path,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(fixed_code)

            generated_files[
                broken_file
            ] = fixed_code

            project_context.add_file(
                broken_file,
                fixed_code
            )

            state.completed_steps.append(
                f"Fixed {broken_file}"
            )

            CodingAgent.emit(
                "Retrying execution..."
            )

            execution = (
                ProjectTool.run_project(
                    project_path,
                    plan["run_command"]
                )
            )

            retry_count += 1

        if execution["success"]:

            CodingAgent.emit(
                "Project executed successfully."
            )

        else:

            CodingAgent.emit(
                "Autonomous debugging failed."
            )

        return {
            "success": execution["success"],
            "project_name": plan[
                "project_name"
            ],
            "project_path": project_path,
            "generated_files": list(
                generated_files.keys()
            ),
            "execution": execution,
            "state": state.to_dict()
        }