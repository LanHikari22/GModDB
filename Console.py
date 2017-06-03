from AbstractCommand import AbstractCommand

class Console:

    # ALL COMMANDS TO OPERATE ON ARE TO BE PUT HERE #
    CMDS = ()

    # File to operate on #
    file = None
    # Appending or Overwriting Signal#
    appendMode = None

    def start(self):
        print(self.CMDS)
        print(self.file)
        while True:
            pass

    def mainRoutine(self):
        pass

    def exec(self, cmd):
        if not issubclass(cmd,AbstractCommand):
            raise TypeError("Invalid command parameter. It must be of type Command")
        pass