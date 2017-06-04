"""
This module's purpose is to construct the commands used in the Console module.
Usage:
    1) Import all necessary modules
    2) Modify the constructCommands() method and input the command you wish to use.
       All commands MUST be inserted before the HelpCmd command, since it depends on all commands being present.
Note:
    You may copy ExitCmd.py into a new command subclass of AbstractCommand if you wish. It has convenient todos on
    each method to change, as well as the class name. This might help if you're lazy
"""

# Import all necessary Modules here
from AbstractCommand import AbstractCommand
from Exceptions import *
from ExitCmd import ExitCmd
from HelpCmd import HelpCmd

"""
Verifies that all commands extend AbstractCommand
If not... An InvalidCommandException is thrown. Please make sure this doesn't happen. Thank you :)
It also verifies that all commands have unique names, else an InvalidCommandException is thrown.
"""
def verify(commands):
    names = [] # will be used to verify all commands have unique names
    for command in commands:
        if not issubclass(command.__class__, AbstractCommand):
            raise InvalidCommandException('command "%s" is not a valid command' % (command.getName()))
        if command.getName() in names:
            raise InvalidCommandException('command "%s" is not the only command with that name' % (command.getName()))
        names.append(command.getName())
    return commands

"""
Put all commands extending AbstractCommand to be used by the Console here

Returns:
    A tuple containing all Commands.
"""
def constructCommands():

    commands = []

    # Insert all commands to the commands list here
    commands.append(ExitCmd())

    # General Help menu for the console. It requires all previous commands, so it must be the last to be added
    commands.append(HelpCmd(tuple(commands)))

    # Verifies that all commands extend AbstractCommand. Raises an exception otherwise.
    return tuple(verify(commands))

# Commands tuple used in the Console #
commands = constructCommands()