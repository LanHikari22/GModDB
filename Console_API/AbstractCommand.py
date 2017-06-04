
"""
This class represents an interface to what a console command is expected to have.
All classes extending this must override ALL METHODS to return appropriate data
"""
class AbstractCommand:

    """
    This method is called when the user executes the command
    """
    def exec(self, *args):
        print("Dude, what you want???")
        print(args)
        print("Yeah, so?? What I do with these?")


    """
    Returns the name of the command that would be identified with in the console.
    """
    def getName(self):
        return "abstract"

    """
    Returns a very brief summary of the command
    Format:
    <command> - <brief Description>
    """
    def getBrief(self):
        return "Abstract - existing in thought or as an idea but not having a physical or concrete existence."

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
        return "I'm an abstract object... What is reality?"

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
        return "I'd write a book about me, but who would buy that? You will... right?"



