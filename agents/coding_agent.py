import os

from agents.planning_agent import PlanningAgent
from agents.file_generation_agent import (
    FileGenerationAgent
)

from agents.debug_agent import DebugAgent

from tools.file_tool import FileTool
from tools.project_tool import ProjectTool

from core.project_state import ProjectState
from core.logger import HelixLogger


class CodingAgent:

    def __init__(self):

        self.logger = HelixLogger("coding")

        self.state = ProjectState()

    def execute(
        self,
        prompt,
        workspace
    ):

        self.logger.log(
            "Creating project plan"
        )

        project_plan = (
            PlanningAgent.create_plan(prompt)
        )

        project_name = (
            project_plan["project_name"]
        )

        project_path = (
            ProjectTool.create_project(
                workspace,
                project_name
            )
        )

        self.state.set_project(project_name)

        self.state.set_project_type(
            project_plan["project_type"]
        )

        self.state.set_run_command(
            project_plan["run_command"]
        )

        self.state.set_dependencies(
            project_plan["dependencies"]
        )

        ProjectTool.create_folder_structure(
            project_path,
            project_plan["files"]
        )

        generated_files = {}

        for file_data in project_plan["files"]:

            file_path = file_data["path"]

            self.logger.log(
                f"Generating {file_path}"
            )

            code = (
                FileGenerationAgent.generate_file(
                    project_prompt=prompt,
                    project_plan=project_plan,
                    current_file=file_data,
                    existing_files=list(
                        generated_files.keys()
                    )
                )
            )

            absolute_path = os.path.join(
                project_path,
                file_path
            )

            FileTool.write(
                absolute_path,
                code
            )

            generated_files[file_path] = code

            self.state.add_generated_file(
                file_path
            )

        self.logger.log(
            "Installing dependencies"
        )

        dependency_result = (
            ProjectTool.install_dependencies(
                project_path,
                project_plan["dependencies"]
            )
        )

        self.logger.log(
            str(dependency_result)
        )

        ProjectTool.create_requirements_file(
            project_path,
            project_plan["dependencies"]
        )

        max_debug_attempts = 5

        for attempt in range(
            max_debug_attempts
        ):

            self.logger.log(
                f"Run Attempt {attempt + 1}"
            )

            run_result = (
                ProjectTool.run_project(
                    project_path,
                    project_plan["run_command"]
                )
            )

            if run_result["success"]:

                self.logger.log(
                    "Project executed successfully"
                )

                return {
                    "success": True,
                    "project_name": project_name,
                    "project_path": project_path,
                    "generated_files": list(
                        generated_files.keys()
                    ),
                    "execution": run_result,
                    "state": self.state.get_state()
                }

            error_output = (
                run_result["stderr"]
            )

            self.logger.log(error_output)

            debug_result = (
                DebugAgent.analyze_error(
                    project_prompt=prompt,
                    project_plan=project_plan,
                    generated_files=generated_files,
                    error_output=error_output
                )
            )

            broken_file = (
                debug_result["broken_file"]
            )

            fix_strategy = (
                debug_result["fix_strategy"]
            )

            self.logger.log(
                f"Broken File: {broken_file}"
            )

            if broken_file not in generated_files:

                self.logger.log(
                    "Broken file not found"
                )

                break

            fixed_code = (
                DebugAgent.fix_file(
                    project_prompt=prompt,
                    broken_file_path=broken_file,
                    broken_file_code=generated_files[
                        broken_file
                    ],
                    error_output=error_output,
                    fix_strategy=fix_strategy
                )
            )

            absolute_path = os.path.join(
                project_path,
                broken_file
            )

            FileTool.write(
                absolute_path,
                fixed_code
            )

            generated_files[
                broken_file
            ] = fixed_code

            self.state.add_completed_step(
                f"Fixed {broken_file}"
            )

        return {
            "success": False,
            "error": "Autonomous debugging failed",
            "state": self.state.get_state()
        }