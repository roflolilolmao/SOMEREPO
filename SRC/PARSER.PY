__author__ = "GABRIEL FREITAS, QUENTIN JEANMONOD"

import ply.yacc as YACC
from enum import Enum
from LEX.PY import TOKENS

import AST

#===============================================================================
#
#                    KEYWORDS, TOKENS, DELIMITERS AND SEPARATORS
#
#===============================================================================

OPERATIONS = {
    #TODO : COMPLETE THE OPERATORS LIST ACCORDING TO SPECIFICATIONS
    }

## OUR CLASS ENUMERATION FOR VAR ACCESS

class VAR_NAMES(Enum):
    UGLY = 0
    OLD = 1
    BLUNT = 2
    DUMB = 3
    FLAT = 4
    TINY = 5
    USELESS = 6
    LAZY = 7
    NAUGHTY = 8
    MACHIAVELLIAN = 9
    STINGY = 10
    MOODY = 11
    SELFISH = 12
    GREEDY = 13
    GULLIBLE = 14
    DOGMATIC = 15

class FUNC_NAMES(Enum):
    BEAUTIFUL = 0
    JOYFUL = 1
    AMAZING = 2
    MESMERIZING = 3
    SEXY = 4
    BRILLIANT = 5
    NICE = 6
    WORTHY = 7
    FUNNY = 8
    LOGICAL = 9
    HELPFUL = 10
    KEEN = 11
    VIGILANT = 12
    BRAVE = 13
    PASSIONATE = 14
    GENEROUS = 15

VARS = {
    
}

#===============================================================================
#
#                         SOMELANGUAGE STRUCTURE DEFINITION
#
#===============================================================================




#===============================================================================
#
#                         SOMELANGUAGE PARSER MAIN FUNCTION
#
#===============================================================================

if __name__ == "__main__":
    import sys

    prog = open(sys.argv[1]).read()
    result = YACC.parse(prog)
    print (result)


