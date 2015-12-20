import ply.yacc as YACC
from LEXICAL import *
from AST import *
# DEBUG
import inspect

__author__ = "GABRIEL FREITAS, QUENTIN JEANMONOD"


# ===============================================================================
#
#                         SOMELANGUAGE STRUCTURE DEFINITION
#
# ===============================================================================

def p_PROGRAM_STATEMENT(P):
    """PROGRAM : STATEMENT DOT"""
    P[0] = ProgramNode(P[1])


def p_PROGRAM_STATEMENT_REC(P):
    """PROGRAM : STATEMENT DOT PROGRAM"""
    P[0] = ProgramNode([P[1]] + P[3].children)


def p_PROGRAM_FUNCTION(P):
    """PROGRAM : FUNCTION PROGRAM"""
    P[0] = ProgramNode([P[1]] + P[2].children)


# ========== FUNCTIONS ==========

def p_FUNC_DECL(P):
    """FUNCTION : SOMEFUNC FUNC IS FUNCBODY LINEBREAK"""
    P[0] = DeclareFunctionNode(P[2], P[4])


def p_FUNCBODY(P):
    """FUNCBODY : STATEMENT DOT"""
    P[0] = ProgramNode([P[1]])


def p_FUNCBODY_RETURN(P):
    """FUNCBODY : RETURN EXPRESSION DOT"""
    P[0] = ProgramNode([ReturnNode(P[2])])


def p_FUNCBODY_REC(P):
    """FUNCBODY : STATEMENT DOT FUNCBODY"""
    P[0] = ProgramNode([P[1]] + P[3].children)


# ========== STATEMENTS ==========

def p_STATEMENT_EXP(P):
    """STATEMENT : ASSIGNMENT
    | PRINT"""
    P[0] = P[1]


def p_ASSIGNEMENT(P):
    """ASSIGNMENT : SOMETHING VAR IS EXPRESSION"""
    P[0] = AssignNode([TokenNode(P[2]), P[4]])


def p_PRINT(P):
    """PRINT : DISPLAY_VAR EXPRESSION"""
    P[0] = PrintNode(P[2])


# ========== EXPRESSIONS ==========

def p_EXPRESSION_NUM(P):
    """EXPRESSION : NUMBER
    | SOMETHING VAR"""
    if len(P) > 2:
        P[0] = TokenNode(P[2])
    else:
        P[0] = TokenNode(P[1])


def p_EXPRESSION_FUNC(P):
    """EXPRESSION : SOMEFUNC FUNC"""
    P[0] = FunctionNode(P[2])


def p_EXPRESSION_OP(P):
    """EXPRESSION : EXPRESSION ADD_OP EXPRESSION
    | EXPRESSION MUL_OP EXPRESSION"""
    P[0] = OpNode(P[2], [P[1], P[3]])


def p_error(P):
    print('PARSER: SYNTAX ERROR: {}'.format(P))
    YACC.yacc().errok()


precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP')
)

# ===============================================================================
#
#                         SOMELANGUAGE PARSER MAIN FUNCTION
#
# ===============================================================================

YACC.yacc()


def PARSE(PROGRAM):
    return YACC.parse(PROGRAM)


if __name__ == "__main__":
    import sys

    PROG = open(sys.argv[1]).read()
    RESULT = PARSE(PROG)
    print('RESULT: {}'.format(RESULT))
    import os
    GRAPH = RESULT.makegraphicaltree()
    NAME = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
    GRAPH.write_pdf(NAME)
    print("WROTE AST TO ", NAME)


