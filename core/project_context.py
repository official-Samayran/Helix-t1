import os
import ast


class ProjectContext:

    def __init__(self):

        self.files = {}

        self.imports = {}

        self.functions = {}

        self.classes = {}

    def add_file(
        self,
        file_path,
        code
    ):

        self.files[file_path] = code

        self.extract_metadata(
            file_path,
            code
        )

    def extract_metadata(
        self,
        file_path,
        code
    ):

        try:

            tree = ast.parse(code)

        except:

            return

        imports = []
        functions = []
        classes = []

        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.Import
            ):

                for alias in node.names:

                    imports.append(
                        alias.name
                    )

            elif isinstance(
                node,
                ast.ImportFrom
            ):

                if node.module:

                    imports.append(
                        node.module
                    )

            elif isinstance(
                node,
                ast.FunctionDef
            ):

                functions.append(
                    node.name
                )

            elif isinstance(
                node,
                ast.ClassDef
            ):

                classes.append(
                    node.name
                )

        self.imports[file_path] = imports

        self.functions[file_path] = functions

        self.classes[file_path] = classes

    def build_context_prompt(self):

        lines = []

        lines.append(
            "PROJECT CONTEXT:"
        )

        for file_path in self.files:

            lines.append(
                f"\nFILE: {file_path}"
            )

            lines.append(
                f"IMPORTS: {self.imports.get(file_path, [])}"
            )

            lines.append(
                f"FUNCTIONS: {self.functions.get(file_path, [])}"
            )

            lines.append(
                f"CLASSES: {self.classes.get(file_path, [])}"
            )

        return "\n".join(lines)

    def get_file_code(
        self,
        file_path
    ):

        return self.files.get(
            file_path,
            ""
        )

    def get_all_files(self):

        return self.files