class ProjectState:

    def __init__(self):

        self.current_project = None

        self.project_type = None

        self.run_command = None

        self.generated_files = []

        self.completed_steps = []

        self.errors = []

        self.dependencies = []

    def set_project(self, name):

        self.current_project = name

    def set_project_type(self, project_type):

        self.project_type = project_type

    def set_run_command(self, command):

        self.run_command = command

    def add_generated_file(self, file_path):

        self.generated_files.append(file_path)

    def add_completed_step(self, step):

        self.completed_steps.append(step)

    def add_error(self, error):

        self.errors.append(error)

    def set_dependencies(self, dependencies):

        self.dependencies = dependencies

    def get_state(self):

        return {
            "project_name": self.current_project,
            "project_type": self.project_type,
            "run_command": self.run_command,
            "generated_files": self.generated_files,
            "completed_steps": self.completed_steps,
            "errors": self.errors,
            "dependencies": self.dependencies
        }

    def clear(self):

        self.current_project = None

        self.project_type = None

        self.run_command = None

        self.generated_files = []

        self.completed_steps = []

        self.errors = []

        self.dependencies = []