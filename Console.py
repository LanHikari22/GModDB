from AbstractCommand import AbstractCommand

class Console:

    # Input all Used commands here #
    CMDS = ()

    def __init__(self, *args):
        pass

    def mainRoutine(self):
        pass

    def exec(self, cmd):
        if not issubclass(cmd,AbstractCommand):
            raise TypeError("Invalid command parameter. It must be of type Command")
        pass