import subprocess


class LiveTerminalTool:

    @staticmethod
    def stream(command, cwd=None):

        process = subprocess.Popen(
            command,
            shell=True,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        for line in iter(
            process.stdout.readline,
            ''
        ):

            yield line

        process.stdout.close()

        process.wait()