class ProjectState:

    def __init__(
        self,
        project_name,
        project_type,
        run_command
    ):

        self.project_name = project_name

        self.project_type = project_type

        self.run_command = run_command

        self.generated_files = []

        self.completed_steps = []

        self.errors = []

        self.dependencies = []

    def to_dict(self):

        return {
            "project_name":
                self.project_name,

            "project_type":
                self.project_type,

            "run_command":
                self.run_command,

            "generated_files":
                self.generated_files,

            "completed_steps":
                self.completed_steps,

            "errors":
                self.errors,

            "dependencies":
                self.dependencies
        }