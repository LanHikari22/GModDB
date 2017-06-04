import sys

# sys.path.insert(0, '/home/lan/Projects/XML_Parser/')
# sys.path.insert(0, '/home/lan/Projects/XML_Writer/')
from Console_API.Console import Console

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
    mode = "a+" if console.appendMode else "w+"
    file = open(filename,mode)
    console.file = file
    if isVerbose:
        mode = "append" if console.appendMode else "overwrite"
        print('console is now operating on "' + filename + '"')


"""
Handles configuring the Console file operating mode
"""
def handleMode(append):
    console.appendMode = append
    if isVerbose:
        mode = "append" if append else "overwrite"
        print("Console is set on %s mode" % (mode))

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
    # Verbose argument checked first to respond to other commands verbosely
    global isVerbose
    if "--verbose" in args or "-v" in args:
        isVerbose = True
    else:
        isVerbose = False
    # If help is executed, the program exits
    if "--help" in args or "-h" in args:
        handleHelp()
    # Handle file mode -- Default: append
    if "--overwrite" in args or "-o" in args:
        handleMode(append=False)
    elif "--append" in args or "-a" in args:
        handleMode(append=True)
    else:
        handleMode(append=True)
    # Handles passed file -- Default: "default.xml"
    try:
        if "--file" in args:
            handleFile(args[args.index("--file")+1])
        elif "-f" in args:
            handleFile(args[args.index("-f")+1])
        else:
            handleFile("default.xml")
    except ValueError:
        print("No filename passed. Please pass the filename to operate on")

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            configureConsole(*sys.argv[1:])
        else: # Setting defaults
            configureConsole()
        console.start()
    except IOError as e   :
        sys.stderr.write(str(e))
    except BaseException as e:
        sys.stderr.write(str(e))

