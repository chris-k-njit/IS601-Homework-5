# Make sure that all command classes are implementing an execute method.
class CommandInterface:
    def execute(self, *args):
        raise NotImplementedError("Command must implement an execute method")
    