import ply.yacc as YACC
from LEXICAL.PY import TOKENS
import AST

__author__ = "GABRIEL FREITAS, QUENTIN JEANMONOD"

# ===============================================================================
#
#                    KEYWORDS, TOKENS, DELIMITERS AND SEPARATORS
#
# ===============================================================================

OPERATIONS = {
    # TODO : COMPLETE THE OPERATORS LIST ACCORDING TO SPECIFICATIONS
    }

# OUR CLASS ENUMERATION FOR VAR ACCESS


VARS = {
    
}

# ===============================================================================
#
#                         SOMELANGUAGE STRUCTURE DEFINITION
#
# ===============================================================================


# ===============================================================================
#
#                         SOMELANGUAGE PARSER MAIN FUNCTION
#
# ===============================================================================


if __name__ == "__main__":
    import sys

    PROG = open(sys.argv[1]).read()
    RESULT = YACC.parse(PROG)
    print(RESULT)


