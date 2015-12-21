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
    """FUNCTION : DECLARE_FUNC SOMEFUNC FUNC COLON FUNCBODY LINEBREAK"""
    P[0] = DeclareFunctionNode(P[3], P[5])


def p_PARAMS(P):
    """PARAMS : EXPRESSION"""
    P[0] = ParamsNode([P[1]])


def p_PARAMS_REC(P):
    """PARAMS : EXPRESSION COMMA PARAMS"""
    P[0] = ParamsNode([P[1]] + P[3].children)


def p_FUNC_DECL_ARGS(P):
    """FUNCTION : DECLARE_FUNC SOMEFUNC FUNC WITH PARAMS COLON FUNCBODY LINEBREAK"""
    P[0] = DeclareFunctionNode(P[3], P[7], P[5])


def p_FUNCBODY(P):
    """FUNCBODY : STATEMENT DOT"""
    P[0] = ProgramNode([P[1]])


def p_FUNCBODY_REC(P):
    """FUNCBODY : STATEMENT DOT FUNCBODY"""
    P[0] = ProgramNode([P[1]] + P[3].children)


# ========== STATEMENTS ==========

def p_STATEMENT_RETURN(P):
    """STATEMENT : RETURN EXPRESSION"""
    P[0] = ReturnNode(P[2])


def p_STATEMENT_EXP(P):
    """STATEMENT : ASSIGNMENT
    | PRINT"""
    P[0] = P[1]


def p_ASSIGNEMENT(P):
    """ASSIGNMENT : SOMETHING VAR IS EXPRESSION
    | SOMETHING VAR SOMEPLACE ACCESSOR IS EXPRESSION"""
    if len(P) > 5:
        # SOMETHING VAR SOMEPLACE ACCESSOR IS EXPRESSION
        P[0] = AssignNode([TokenNode(P[2], P[4]),  P[6]])
    else:
        # SOMETHING VAR IS EXPRESSION
        P[0] = AssignNode([TokenNode(P[2]), P[4]])


def p_PRINT(P):
    """PRINT : DISPLAY_VAR EXPRESSION
    | DISPLAY_VAR ASCII EXPRESSION"""
    P[0] = PrintNode(P[3 if len(P) > 3 else 2], len(P) > 3)


# ========== EXPRESSIONS ==========

def p_EXPRESSION_NUM(P):
    """EXPRESSION : NUMBER
    | SOMETHING VAR
    | SOMETHING VAR SOMEPLACE ACCESSOR"""
    if len(P) == 2:
        # NUMBER
        P[0] = TokenNode(P[1])
    elif len(P) == 3:
        # SOMETHING VAR
        P[0] = TokenNode(P[2])
    else:  # len(P) == 5:
        # SOMETHING VAR SOMEPLACE ACCESSOR
        P[0] = [TokenNode(P[2], P[4])]


def p_EXPRESSION_FUNC(P):
    """EXPRESSION : SOMEFUNC FUNC"""
    P[0] = FunctionNode(P[2])


def p_EXPRESSION_FUNC_PARAMS(P):
    """EXPRESSION : SOMEFUNC FUNC COMMA FUNC_PARAMS COLON PARAMS"""
    P[0] = FunctionNode(P[2], P[6])


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
    NAME = os.path.splitext(sys.argv[1])[0] + '-ast.pdf'
    GRAPH.write_pdf(NAME)
    print("WROTE AST TO ", NAME)
