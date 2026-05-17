import os
import subprocess
import webbrowser


class ExecutionRouter:

    @staticmethod
    def execute(
        project_type,
        project_path,
        run_command
    ):

        ptype = (
            project_type.lower()
        )

        if (
            "html" in ptype
            or "javascript" in ptype
            or "css" in ptype
        ):

            index_path = os.path.join(
                project_path,
                "index.html"
            )

            webbrowser.open(
                index_path
            )

            return {
                "success": True,
                "stdout":
                    "HTML project opened in browser.",
                "stderr": ""
            }

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

        return {
            "success":
                process.returncode == 0,

            "stdout": stdout,

            "stderr": stderr
        }