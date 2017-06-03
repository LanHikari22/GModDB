import sys
sys.path.insert(0, '/home/lan/Projects/XML_Parser/')
sys.path.insert(0, '/home/lan/Projects/XML_Writer/')

from XMLWriter import *
from AbstractXMLWriterHandler import *
from XMLParser import *
from AbstractXMLParserHandler import *
from XMLTag import XMLTag
from Console import Console

console = Console()

def processArgs():
    pass

if __name__ == '__main__':

    if len(sys.argv) > 1:
        processArgs()

