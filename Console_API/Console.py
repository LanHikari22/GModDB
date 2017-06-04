"""
To modify this program, please head to the ConsoleCommmands module for instructions.
Things that you may modify in this module:
    - Initial print in start()
    - environmentPrompt()
Minimum files needed for the Console API:
    - Console.py
    - ConsoleCommands.py
    - Exceptions.py
    - ExitCmd.py
    - HelpCmd.py
"""
from Console_API import ConsoleCommands


class Console:

    # All Commands used within the console. Must extend AbstractCommand #
    commands = ConsoleCommands.commands

    # File to operate on #
    file = None
    # Appending or Overwriting Signal#
    appendMode = None

    """
    Initiates the console environment
    """
    def start(self):
        print('Welcome to the Game Modding Database! Written by yours truly, Lan! Enter "help" to display all commands')
        while True:
            userStr = input(self.environmentPrompt() + ' ')
            argv = self.parse(userStr)
            self.exec(*argv)

    """"
    Attempts to execute a command from arguments passed from the user
    """
    def exec(self, *argv):
        # We better have any arguments to execute them
        if argv:
            # Create the appropriate command based on args[0]
            cmd = None
            name = argv[0]
            for command in self.commands:
                if name == command.getName():
                    cmd = command
            if not cmd:
                print("Command %s does not exist" % name)
            else:
                # Execute the specific command's action, and pass it the rest of the args
                cmd.exec(*argv[1:])


    """
    Modify this to change the applications user prompt text.
    """
    def environmentPrompt(self):
        return "GMDB@%s>" % (self.file.name)

    """
    Parses space delimited elements from a string to a list.
    If there is text between quotes '"', all of that text is captured as one element
    """
    def parse(self, s):
        args = []
        temp = ""
        openQuotes = False
        for c in s.strip():
            if c.isspace() and not openQuotes:
                args.append(temp)
                temp = ""
            elif c != '"':
                temp += c
            elif c == '"':
                openQuotes = not openQuotes
        if temp:
            args.append(temp)
        return args