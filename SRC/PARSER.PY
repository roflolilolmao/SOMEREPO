__author__ = "GABRIEL FREITAS, QUENTIN JEANMONOD"

import ply.yacc as YACC
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

VARS = {
    #TODO : LIMIT THE AMOUNT OF AVAILABLE VARIABLES
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


