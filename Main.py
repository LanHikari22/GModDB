import sys
import Main
sys.path.insert(0, '/home/lan/Projects/XML_Parser/')
sys.path.insert(0, '/home/lan/Projects/XML_Writer/')
from XMLWriter import *
from AbstractXMLWriterHandler import *
from XMLParser import *
from AbstractXMLParserHandler import *
from XMLTag import XMLTag
from Console import Console

# Console Object to operate on #
console = Console()
# Signal determining whether to inform the user of initiation action or not #
isVerbose = False

"""
Handles The case when the user passes an argument asking for help!
"""
def handleHelp():
    if isVerbose: print("Displaying the help menu")
    print(
'''Configures the Console based on passed arguments.

[Arguments]
Note: All following commands have a shorter version being their initial.
ex: --help and -h are the same. --file <filename> and -f <filename> also.
--help            
| Displays this very menu and then exits the program!
--file <filename> 
| Selects database file to operate on. Extension doesn't matter, but the format should be XML.
--overwrite       
| Sets the writing mode to overwrite. The file would be formatted, if it existed.
--append          
| Keeps the data in the file. This is the default option.
--verbose         
| Informs user when performing a console initiation action. Console Program is not affected.

[Default Behavior]
If no file is selected, and the append/overwrite mode is not set, the program would default to append mode.
the user will be prompted within the console program to input a file path, or just operate on a default file.
''')
    exit(0)

"""
Handles configuring the Console operating file.
"""
def handleFile(filename):
    # todo handle
    # todo verbose
    pass

"""

"""
def handleMode(append):
    # todo handle
    # todo verbose
    pass

'''
Configures the Console based on passed arguments.

[Possible arguments]
Note: All following commands have a shorter version being their initial.
ex: --help and -h are the same. --file <filename> and -f <filename> also.
--help              | Displays this very menu and then exits the program!
--file <filename>   | Selects database file to operate on. Extension doesn't matter, but the format should be XML.
--overwrite         | Sets the writing mode to overwrite. The file would be formatted, if it existed.
--append            | Keeps the data in the file. This is the default option.
--verbose           | Informs user when performing a console initiation action. Console Program is not affected.

[Default Behavior]
If no file is selected, and the append/overwrite mode is not set, the program would default to append mode.
the user will be prompted within the console program to input a file path, or just operate on a default file.
'''
def configureConsole(*args):
    if "--verbose" in args or "-v" in args:
        isVerbose = True
    # else:
    #     isVerbose = False
    for i in range(len(args)):
        if isVerbose:
            print("[%u] %s" % (i, args[i]))
        if args[i] == "--help" or args[i] == "-h":
            handleHelp()
        if args[i] == "--file" or args[i] == "-f":
            if i+1 < len(args):
                handleFile(args[i+1])
            else:
                print("No filename passed. Please pass the filename to operate on")
        if args[i] == "--overwrite" or args[i] == "-o":
            handleMode(append=False)
        if args[i] == "--append" or args[i] == "-a":
            handleMode(append=True)

    pass

if __name__ == '__main__':
    staticfunction()
    try:
        if len(sys.argv) > 1:
            configureConsole(*sys.argv[1:])
    except IOError as e   :
        sys.stderr.write(str(e))
    except BaseException as e:
        sys.stderr.write(str(e))

