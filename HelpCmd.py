from AbstractCommand import AbstractCommand
from Exceptions import *
class HelpCmd(AbstractCommand):

    # Tuple of commands to show the documentation of #
    commands= None
    # name of the command #
    name = None

    def __init__(self, commands):
        if commands.__class__ != tuple:
            raise InvalidCommandException("Commands passed to the HelpCmd object are not a tuple")
        self.commands = commands
        self.commands += (self,)
        self.name = self.getName()


    """
    This method is called when the user executes the command
    """
    def exec(self, *args):
        if len(args) > 2:
            print("%s: invalid arguments" % (self.name))
        elif len(args) > 1 and (args[0] == "-d" or args[0] == "--doc"):
            commandAvailable = False
            for command in self.commands:
                if args[1] == command.getName():
                    commandAvailable = True
                    print(command.getDoc())
                if not commandAvailable:
                    print("Command %s does not exist" % (args[1]))
        elif len(args) > 0:
            commandAvailable = False
            for command in self.commands:
                if args[0] == command.getName():
                    commandAvailable = True
                    print(command.getSynp())
                if not commandAvailable:
                    print("Command %s does not exist" % (args[0]))
        else:
            print("Available Commands:")
            for command in self.commands:
                print(command.getBrief())

    """
    Returns the name of the command that would be identified with in the console.
    """
    def getName(self):
        return "help"

    """
    Returns a very brief summary of the command
    Format:
    <command> - <brief Description>
    """
    def getBrief(self):
        return "%s - Tries its very best to help you understand this program :)" % self.name

    """
    returns syntactical documentation about the command
    Format:    
    NAME
        <command> - <brief Description>
    SYNPOSIS
        <command> [optionalArg] requiredArg
        <command> [option1 | option2 | option3] requiredArg
    """
    def getSynp(self):
        # todo verify
        synp = "NAME"
        synp += "\n\t" + self.getBrief()
        synp += "\nSYNPOSIS"
        synp += """
    %s
    %s [-d | --doc] command""" % (self.name,self.name)
        return synp

    """
    Returns full documentation of the command.
    Format:    
    NAME
        <command> - <brief Description>
    SYNPOSIS
        <command> [optionalArg] requiredArg
        <command> [option1 | option2 | option3] requiredArg
    ARGUMENTS
        <arg1>: <description>
        <arg2>[|[arg2_alternate_name]]: <description>
    DESCRIPTION
    <Describe command in details here>
    """
    def getDoc(self):
        # todo verify
        doc = self.getSynp()
        doc += "\nARGUMENTS"
        doc += """
    No args: Displays very brief summary of all commands
    command: Name of the command to be displayed
    -d|--doc: Displays full documentaton of a command"""
        doc += "\nDESCRIPTION"
        doc += """
    The %s command can display all available commands, or a command can be specified so it displays
    more syntactical details regarding the command. 
    Full documentation of the comman may also be displayed.""" % self.name
        return doc