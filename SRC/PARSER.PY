import ply.yacc as YACC
from LEXICAL import *
from AST import *

__author__ = "GABRIEL FREITAS, QUENTIN JEANMONOD"

# ===============================================================================
#
#                    KEYWORDS, TOKENS, DELIMITERS AND SEPARATORS
#
# ===============================================================================

operations = {
    'PLUS': lambda X, Y: X + Y,
    'MINUS': lambda X, Y: X - Y,
    'BY': lambda X, Y: X * Y,
    'OUT OF': lambda X, Y: X / Y
}

# OUR CLASS ENUMERATION FOR VAR ACCESS

VARS = {
    
}

FUNCS = {

}

# ===============================================================================
#
#                         SOMELANGUAGE STRUCTURE DEFINITION
#
# ===============================================================================


def p_PROGRAM_STATEMENT(P):
    '''PROGRAM : STATEMENT
    | STATEMENT DOT PROGRAM'''
    if len(P) > 2:
        P[0] = ProgramNode([P[1]] + P[3].children)
    else:
        P[0] = ProgramNode(P[1])


def p_STATEMENT_EXP(P):
    '''STATEMENT : ASSIGNMENT'''
    # | STRUCTURE'''
    P[0] = P[1]


def p_ASSIGNEMENT(P):
    '''ASSIGNMENT : SOMETHING VAR IS EXPRESSION'''
    P[0] = AssignNode([TokenNode(P[2]), P[4]])


def p_EXPRESSION_NUM(P):
    '''EXPRESSION : NUMBER
    | SOMETHING VAR'''
    if len(P) > 2:
        P[0] = TokenNode(P[2])
    else:
        # USE VAR{}
        P[0] = TokenNode(P[1])


def p_EXPRESSION_OP(P):
    '''EXPRESSION : EXPRESSION ADD_OP EXPRESSION
    | EXPRESSION MUL_OP EXPRESSION'''
    P[0] = OpNode(P[2], [P[1], P[3]])


def p_error(P):
    print('PARSER: SYNTAX ERROR: {}'.format(P))
    YACC.yacc().errok()


# ===============================================================================
#
#                         SOMELANGUAGE PARSER MAIN FUNCTION
#
# ===============================================================================

YACC.yacc()

if __name__ == "__main__":
    import sys

    PROG = open(sys.argv[1]).read()
    RESULT = YACC.parse(PROG)
    print(RESULT)


