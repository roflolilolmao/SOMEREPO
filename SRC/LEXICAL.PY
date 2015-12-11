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
    # 'SHOW',
    # 'ME',
    # 'WHAT',
    # 'COULD',
    # 'BE',
    'OUT',
    'OF',
    'PLUS',
    'MINUS',
    'BY'
    )

tokens = (
    'DOT',
    # 'COMMA',
    # 'SEMICOLON',
    # 'LINEBREAK',
    'VAR',
    # 'FUNC',
    'NUMBER'
    ) + tuple(map(lambda S: S.upper(), RESERVED_WORDS))
t_DOT = r'\.'
# t_COMMA = r','
# t_SEMICOLON = r';'
# t_LINEBREAK = r'\n'

# ===============================================================================
#
#                                 PARSER ANALYSERS
#
# ===============================================================================


def t_WORDS(T):
    r'[A-Za-z_]\w*'
    if T.value in RESERVED_WORDS:
        T.type = T.value.upper()
    elif T.value in VAR_NAMES:
        T.type = 'VAR'
    elif T.value in FUNC_NAMES:
        T.type = 'FUNC'
    else:
        t_error(T)
    return T


def t_NUMBER(T):
    r'\d+(\.\d+)?'
    try:
        T.value = int(T.value)
    except ValueError:
        try:
            T.value = float(T.value)
        except ValueError:
            print('VALUE ERROR THIS IS NOT A FLOAT')
    return T


t_ignore = ' \t'


def t_error(T):
    print("LEX: ILLEGAL CHARACTER '%s'" % T.value[0])
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
