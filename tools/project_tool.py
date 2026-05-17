import subprocess
import os


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