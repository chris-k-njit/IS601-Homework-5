class CommandInterface:
    def execute(self, *args):
        raise NotImplementedError("Command must implement an execute method")
    