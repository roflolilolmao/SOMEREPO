import ply.lex as LEX

__author__ = "GABRIEL FREITAS, QUENTIN JEANMONOD"

# ===============================================================================
#
#                      KEYWORDS, TOKENS, DELIMITERS AND SEPARATORS
#
# ===============================================================================


VAR_NAMES = (
    'UGLY',
    'OLD',
    'BLUNT',
    'DUMB',
    'FLAT',
    'TINY',
    'USELESS',
    'LAZY',
    'NAUGHTY',
    'MACHIAVELLIAN',
    'STINGY',
    'MOODY',
    'SELFISH',
    'GREEDY',
    'GULLIBLE',
    'DOGMATIC'
)

FUNC_NAMES = (
    'BEAUTIFUL',
    'JOYFUL',
    'AMAZING',
    'MESMERIZING',
    'SEXY',
    'BRILLIANT',
    'NICE',
    'WORTHY',
    'FUNNY',
    'LOGICAL',
    'HELPFUL',
    'KEEN',
    'VIGILANT',
    'BRAVE',
    'PASSIONATE',
    'GENEROUS'
)


RESERVED_WORDS = (
    'SOMETHING',
    # 'SOMEONE',
    # 'SOMEBODY',
    # 'SOMEWHAT',
    # 'SOMEWAY',
    # 'SOMETIMES',
    # 'SOMEHOW',
    # 'SOMEPLACE',
    'IS',
    # 'COULD',
    # 'BE',
)

tokens = (
    'DOT',
    # 'COMMA',
    # 'SEMICOLON',
    'LINEBREAK',
    'VAR',
    'FUNC',
    'SOMEFUNC',
    'NUMBER',
    'ADD_OP',
    'MUL_OP',
    'DISPLAY_VAR',
    # 'WORDS'
) + tuple(map(lambda S: S.upper(), RESERVED_WORDS))

t_DOT = r'\.'
# t_COMMA = r','
# t_SEMICOLON = r';'
t_LINEBREAK = r'\n'
# t_SOMEFUNC = r'SOMEONE|SOMEBODY'

# ===============================================================================
#
#                                 PARSER ANALYSERS
#
# ===============================================================================


def t_SOMEFUNC(T):
    r"""SOMEONE|SOMEBODY"""
    return T


def t_ADD_OP(T):
    r"""PLUS|MINUS"""
    return T


def t_MUL_OP(T):
    r"""BY|OUT\ OF"""
    return T


def t_DISPLAY_VAR(T):
    r"""SHOW\ ME\ WHAT\ IS"""
    return T


def t_NUMBER(T):
    r"""\d+(\.\d+)?"""
    try:
        T.value = int(T.value)
    except ValueError:
        try:
            T.value = float(T.value)
        except ValueError:
            print('VALUE ERROR THIS IS NOT A NUMBER')
    return T


# MUST BE AT THE END BECAUSE OUR OPERATORS AND OTHER COMPOSED IDENTIFIERS ARE WORD BASED
def t_WORDS(T):
    r"""[A-Za-z_]\w*"""
    if T.value in RESERVED_WORDS:
        T.type = T.value
    elif T.value in VAR_NAMES:
        T.type = 'VAR'
    elif T.value in FUNC_NAMES:
        T.type = 'FUNC'
    else:
        t_error(T)
    return T


t_ignore = ' \t'


def t_error(T):
    print("LEX: ILLEGAL WORD '%s'" % T.value)
    T.lexer.skip(1)

# ===============================================================================
#
#                               LEXEMS MAIN FUNCTION
#
# ===============================================================================

LEX.lex()


if __name__ == "__main__":
    import sys
    PROG = open(sys.argv[1]).read()

    LEX.input(PROG)

    while 1:
        TOKEN = LEX.token()
        if not TOKEN:
            break
        print("LINE {} {} ({})".format(TOKEN.lineno, TOKEN.type, TOKEN.value))
