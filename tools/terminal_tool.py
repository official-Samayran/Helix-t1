import subprocess


class TerminalTool:

    @staticmethod
    def execute(command, cwd=None):

        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=cwd
        )

        stdout, stderr = process.communicate()

        return {
            "success": process.returncode == 0,
            "stdout": stdout,
            "stderr": stderr
        }