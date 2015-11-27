__author__ = "GABRIEL FREITAS, QUENTIN JEANMONOD"

import ply.lex as LEX

#===============================================================================
#
#                      KEYWORDS, TOKENS, DELIMITERS AND SEPARATORS
#
#===============================================================================

RESERVED_WORDS = (
    #TODO : COMPLETE THE LIST OF KEYWORDS
    )

TOKENS = (
    #TODO : COMPLETE THE LIST OF TOKENS
    )

#TODO : COMPLETE THE LIST OF PUNCTUATION LITERALS
LITERALS = ""


#===============================================================================
#
#                                 PARSER ANALYSERS
#
#===============================================================================


#===============================================================================
#
#                               LEXEMS MAIN FUNCTION
#
#===============================================================================
if __name__ == "__main__":
    import sys
    prog = open(sys.argv[1]).read()

    LEX.input(prog)

    while 1:
        TOKEN = LEX.token()
        if not TOKEN:
            break
        print ("LINE %d %s(%s)" % (TOKEN.lineno, TOKEN.TYPE, TOKEN.value))