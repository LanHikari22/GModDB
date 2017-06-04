from AbstractCommand import AbstractCommand
from Exceptions import *

# todo change
class ExitCmd(AbstractCommand):


    """
    This method is called when the user executes the command
    """
    def exec(self, *args):
        # todo change
        if args:
            print("Dunno what additional commands you gave me, but i'll just exit")
        print("Exiting program... Have a nice day!")
        exit('')

    """
    Returns the name of the command that would be identified with in the console.
    """
    def getName(self):
        # todo change
        return "exit"

    """
    Returns a very brief summary of the command
    Format:
    <command> - <brief Description>
    """
    def getBrief(self):
        # todo change
        return "%s - Exits the program" % self.getName()

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
        # todo change
        synp = "NAME"
        synp += "\n\t" + self.getBrief()
        synp += "\nSYNPOSIS"
        synp += """
    %s""" % (self.getName())
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
        # todo change
        doc = self.getSynp()
        doc += "\nARGUMENTS"
        doc += """
    No args: Exits the program
    args: Nothing, really."""
        doc += "\nDESCRIPTION"
        doc += """
    The %s Command Exits the program""" % self.getName()
        return doc