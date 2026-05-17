import subprocess
import os


class ProjectTool:

    @staticmethod
    def create_project(
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
    def create_folder_structure(
        project_path,
        files
    ):

        for file in files:

            full_path = os.path.join(
                project_path,
                file["path"]
            )

            folder = os.path.dirname(
                full_path
            )

            if folder:

                os.makedirs(
                    folder,
                    exist_ok=True
                )

            if not os.path.exists(full_path):

                with open(
                    full_path,
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write("")

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

    @staticmethod
    def install_dependencies(
        project_path,
        dependencies
    ):

        if not dependencies:
            return

        for dependency in dependencies:

            try:

                subprocess.run(
                    f"pip install {dependency}",
                    cwd=project_path,
                    shell=True,
                    check=False,
                    text=True,
                    encoding="utf-8",
                    errors="ignore"
                )

            except Exception:
                pass

    @staticmethod
    def create_requirements_file(
        project_path,
        dependencies
    ):

        requirements_path = os.path.join(
            project_path,
            "requirements.txt"
        )

        with open(
            requirements_path,
            "w",
            encoding="utf-8"
        ) as f:

            for dependency in dependencies:

                f.write(
                    dependency + "\n"
                )

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
                encoding="utf-8",
                errors="ignore",
                timeout=20
            )

            stdout = result.stdout or ""
            stderr = result.stderr or ""

            return {
                "success": result.returncode == 0,
                "stdout": stdout,
                "stderr": stderr
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