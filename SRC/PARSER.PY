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
    P[0] = DeclareFunctionNode(P[3], [ParamsNode([]), P[5]])


def p_FUNC_DECL_ARGS(P):
    """FUNCTION : DECLARE_FUNC SOMEFUNC FUNC WITH PARAMS COLON FUNCBODY LINEBREAK"""
    P[0] = DeclareFunctionNode(P[3], [P[5], P[7]])


def p_PARAMS(P):
    """PARAMS : EXPRESSION"""
    P[0] = ParamsNode([P[1]])


def p_PARAMS_REC(P):
    """PARAMS : EXPRESSION COMMA PARAMS"""
    P[0] = ParamsNode([P[1]] + P[3].children)


def p_FUNCBODY(P):
    """FUNCBODY : STATEMENT DOT"""
    P[0] = ProgramNode([P[1]])


def p_FUNCBODY_REC(P):
    """FUNCBODY : STATEMENT DOT FUNCBODY"""
    P[0] = ProgramNode([P[1]] + P[3].children)


def p_FUNC_PARAMS(P):
    """FUNC_CALL : SOMEFUNC FUNC COMMA FUNC_PARAMS COLON PARAMS"""
    P[0] = FunctionNode(P[2], [P[6]])


def p_FUNC(P):
    """FUNC_CALL : SOMEFUNC FUNC"""
    P[0] = FunctionNode(P[2], [ParamsNode([])])


# ========== STATEMENTS ==========

def p_STATEMENT_RETURN(P):
    """STATEMENT : RETURN EXPRESSION"""
    P[0] = ReturnNode([P[2]])


def p_STATEMENT_CALL(P):
    """STATEMENT : CALL FUNC_CALL"""
    P[0] = P[2]


def p_STATEMENT_EXP(P):
    """STATEMENT : ASSIGNMENT
    | PRINT
    | BLOCK"""
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
    """PRINT : DISPLAY_VAR EXPRESSION"""
    P[0] = PrintNode(P[2])


def p_MAP(P):
    """STATEMENT : EXPLORE SOMETHING VAR WITH SOMEFUNC FUNC"""
    P[0] = MapNode([P[3], FunctionNode(P[6], ParamsNode([])), ParamsNode([])])


def p_MAP_PARAMS(P):
    """STATEMENT : EXPLORE SOMETHING VAR WITH SOMEFUNC FUNC COMMA FUNC_PARAMS COLON PARAMS"""
    P[0] = MapNode([P[3], FunctionNode(P[6], ParamsNode([])), P[10]])


# ========== BLOCKS ==========

def p_IF_BUT(P):
    """BLOCK : SOMEHOW EXPRESSION COLON PROGRAM BUT PROGRAM SOMOFIT"""
    P[0] = SomehowNode([P[2], P[4], P[6]])


def p_IF(P):
    """BLOCK : SOMEHOW EXPRESSION COLON PROGRAM SOMOFIT"""
    P[0] = SomehowNode([P[2], P[4], ProgramNode([])])


def p_WHILE(P):
    """BLOCK : WHILE EXPRESSION COLON PROGRAM END_WHILE"""
    P[0] = WhileNode([P[2], P[4]])


# ========== EXPRESSIONS ==========

def p_EXPRESSION_ASCII(P):
    """EXPRESSION : ASCII EXPRESSION"""
    P[0] = AsciiNode([P[2]])


def p_EXPRESSION_NUM(P):
    """EXPRESSION : NUMBER
    | SOMETHING VAR SOMEPLACE ACCESSOR
    | SOMETHING VAR"""
    if len(P) == 2:
        # NUMBER
        P[0] = TokenNode(P[1])
    elif len(P) == 3:
        # SOMETHING VAR
        P[0] = TokenNode(P[2])
    else:  # len(P) == 5:
        # SOMETHING VAR SOMEPLACE ACCESSOR
        P[0] = TokenNode(P[2], P[4])


def p_FUNC_CALL_EXPRESSION(P):
    """EXPRESSION : FUNC_CALL"""
    P[0] = P[1]


def p_EXPRESSION_BOOLEAN(P):
    """EXPRESSION : SOMEWHAT BOOLEAN"""
    if P[2][:2] != 'UN':
        P[0] = TokenNode(True)
    else:
        P[0] = TokenNode(False)


def p_EXPRESSION_EXISTENCE(P):
    """ EXPRESSION : EXPRESSION EXISTS VAR"""
    P[0] = ExistenceNode(P[1], P[3])


def p_EXPRESSION_COMPARE(P):
    """ EXPRESSION : EXPRESSION COMPARE_OP EXPRESSION"""
    P[0] = CompareNode(P[2], [P[1], P[3]])


def p_EXPRESSION_OP(P):
    """EXPRESSION : EXPRESSION ADD_OP EXPRESSION
    | EXPRESSION MUL_OP EXPRESSION"""
    P[0] = OpNode(P[2], [P[1], P[3]])


def p_error(P):
    print('PARSER: SYNTAX ERROR: {}'.format(P))
    YACC.yacc().errok()


precedence = (
    ('left', 'COMPARE_OP'),
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('left', 'ASCII'),
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

    with open(sys.argv[1]) as PROG:
        RESULT = PARSE(PROG.read())
    print('RESULT: {}'.format(RESULT))
