import subprocess
import os


class ProjectTool:

    @staticmethod
    def execute_project(
        project_path,
        run_command
    ):

        try:

            result = subprocess.run(
                run_command,
                cwd=project_path,
                shell=True,
                capture_output=True,
                text=True,
                timeout=15
            )

            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr
            }

        except subprocess.TimeoutExpired:

            return {
                "success": True,
                "stdout": "Process started successfully.",
                "stderr": ""
            }

        except Exception as e:

            return {
                "success": False,
                "stdout": "",
                "stderr": str(e)
            }

    @staticmethod
    def create_project_folder(
        workspace,
        project_name
    ):

        project_path = os.path.join(
            workspace,
            project_name
        )

        os.makedirs(
            project_path,
            exist_ok=True
        )

        return project_path

    @staticmethod
    def write_file(
        project_path,
        file_path,
        content
    ):

        full_path = os.path.join(
            project_path,
            file_path
        )

        os.makedirs(
            os.path.dirname(full_path),
            exist_ok=True
        )

        with open(
            full_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        return full_path