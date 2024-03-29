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

VAR_ACCESSORS = (
    'DUSTY',
    'GLOOMY',
    'CHARMING',
    'CROWDED',
    'POPULAR',
    'BURLESQUE',
    'DARK',
    'STORMY',
    'NOISY',
    'ANCIENT',
    'DRY',
    'DESERTIC',
    'BUSTLING',
    'POLLUTED',
    'LIVELY',
    'PICTURESQUE'
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
    'SOMEWHAT',
    # 'SOMEWAY',
    'SOMEPLACE',
    'IS',
    'WITH',
    'EXPLORE',
    'CALL',
    'SEAT',
    'OF',
    'AND',
    'OR',
    'NOT'
)

tokens = (
    'DOT',
    'COMMA',
    'COLON',
    # 'SEMICOLON',
    'LINEBREAK',
    'VAR',
    'ACCESSOR',
    'LIST_ACCESSOR',
    'LIST_SETTER',
    'FUNC',
    'SOMEFUNC',
    'RETURN',
    'BOOLEAN',
    'EXISTS',
    'NUMBER',
    'ADD_OP',
    'MUL_OP',
    'COMPARE_OP',
    'DISPLAY_VAR',
    'DECLARE_FUNC',
    'FUNC_PARAMS',
    'SOMEHOW',
    'WHILE',
    'ASCII',
    'SOMOFIT',
    'END_WHILE',
    'BUT'
    # 'WORDS'
) + tuple(map(lambda S: S.upper(), RESERVED_WORDS))

t_DOT = r'\.'
t_COMMA = r','
t_COLON = r':'
# t_SEMICOLON = r';'
t_LINEBREAK = r'\n'


# ===============================================================================
#
#                                 PARSER ANALYSERS
#
# ===============================================================================

def t_BUT(T):
    r"""BUT:"""
    return T


def t_SOMEHOW(T):
    r"""SOMEHOW,"""
    return T


def t_WHILE(T):
    r"""FOR\ SOMETIMES,"""
    return T


def t_END_WHILE(T):
    r"""THIS\ KEPT\ GOING\ ON"""
    return T


def t_SOMOFIT(T):
    r"""SOME\ OF\ IT\ IS\ REAL"""
    return T


def t_SOMEFUNC(T):
    r"""SOMEONE|SOMEBODY"""
    return T


def t_ADD_OP(T):
    r"""PLUS|MINUS"""
    return T


def t_COMPARE_OP(T):
    r"""(GREATER|SMALLER)\ THAN
    | EQUAL\ TO"""
    return T


def t_MUL_OP(T):
    r"""BY|OUT\ OF"""
    return T


def t_LIST_ACCESSOR(T):
    r"""SOMEWHERE\ ORDERED"""
    return T


def t_LIST_SETTER(T):
    r"""IS\ RESPECTIVELY"""
    return T


def t_BOOLEAN(T):
    r"""REAL|UNREAL"""
    return T


def t_EXISTS(T):
    r"""COULD\ BE"""
    return T


def t_DISPLAY_VAR(T):
    r"""SHOW\ ME"""
    return T


def t_ASCII(T):
    r"""SOME\ STYLE\ FOR"""
    return T


def t_DECLARE_FUNC(T):
    r"""HERE\'S"""
    return T


def t_FUNC_PARAMS(T):
    r""",\ DO\ THE\ THING\ WITH\ (THAT\ ONE|THOSE\ ONES)"""
    return T


def t_RETURN(T):
    r"""GIVE\ ME"""
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


def t_COMMENTS(T):
    r"""\(.*\)"""
    print(T)
    pass


# MUST BE AT THE END BECAUSE OUR OPERATORS AND OTHER COMPOSED IDENTIFIERS ARE WORD BASED
def t_WORDS(T):
    r"""[A-Za-z_]\w*"""
    if T.value in RESERVED_WORDS:
        T.type = T.value
    elif T.value in VAR_NAMES:
        T.type = 'VAR'
    elif T.value in VAR_ACCESSORS:
        T.type = 'ACCESSOR'
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


def REMOVECOMMENTS(s):
    sp = ''
    remove = 0
    for c in s:
        if c == '(':
            remove += 1
        if remove < 1:
            sp += c
        if c == ')':
            remove -= 1 if remove > 0 else 0
    return sp


if __name__ == "__main__":
    import sys

    with open(sys.argv[1]) as PROG:
        RESULT = PROG.read()

    RESULT = REMOVECOMMENTS(RESULT)
    LEX.input(RESULT)

    while 1:
        TOKEN = LEX.token()
        if not TOKEN:
            break
        print("LINE {} {} ({})".format(TOKEN.lineno, TOKEN.type, TOKEN.value))
