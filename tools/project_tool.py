import os
import subprocess


class ProjectTool:

    ERROR_KEYWORDS = [
        "traceback",
        "error",
        "exception",
        "failed",
        "invalid",
        "problem"
    ]

    @staticmethod
    def create_project(
        base_path,
        project_name
    ):

        project_path = os.path.join(
            base_path,
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

    @staticmethod
    def install_dependencies(
        project_path,
        dependencies
    ):

        if not dependencies:

            return {
                "success": True,
                "stdout": "",
                "stderr": ""
            }

        deps = " ".join(
            dependencies
        )

        command = (
            f"pip install {deps}"
        )

        process = subprocess.Popen(
            command,
            shell=True,
            cwd=project_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = (
            process.communicate()
        )

        return {
            "success":
                process.returncode == 0,
            "stdout": stdout,
            "stderr": stderr
        }

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

            for dep in dependencies:

                f.write(dep + "\n")

        return requirements_path

    @staticmethod
    def detect_runtime_failure(
        stdout,
        stderr
    ):

        combined = (
            stdout + stderr
        ).lower()

        for keyword in (
            ProjectTool.ERROR_KEYWORDS
        ):

            if keyword in combined:

                return True

        return False

    @staticmethod
    def run_project(
        project_path,
        run_command
    ):

        process = subprocess.Popen(
            run_command,
            shell=True,
            cwd=project_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = (
            process.communicate()
        )

        runtime_failed = (
            ProjectTool.detect_runtime_failure(
                stdout,
                stderr
            )
        )

        success = (
            process.returncode == 0
            and not runtime_failed
        )

        return {
            "success": success,
            "stdout": stdout,
            "stderr": stderr
        }