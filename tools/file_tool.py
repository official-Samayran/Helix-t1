import os


class FileTool:

    @staticmethod
    def write(path, content):
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return "File written successfully"

    @staticmethod
    def read(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()