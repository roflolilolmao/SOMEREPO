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
    'IDENTIFIER',
    'SOMETHING',
    'SOMEONE',
    'SOMEBODY',
    'SOMEWHAT',
    'SOMEWAY',
    'SOMETIMES',
    'SOMEHOW',
    'SOMEPLACE',
    'IS',
    'SHOW ME WHAT',
    'COULD BE'
    )

TOKENS = (
    'DOT',
    'COMMA',
    'SEMICOLON',
    'LINEBREAK',
    'VAR',
    'FUNC'
    ) + tuple(map(lambda S: S.upper(), RESERVED_WORDS + FUNC_NAMES + VAR_NAMES))

t_DOT = r'\.'
t_COMMA = r','
t_SEMICOLON = r';'
t_LINEBREAK = r'\n'

# ===============================================================================
#
#                                 PARSER ANALYSERS
#
# ===============================================================================


def t_IDENTIFIER(t):
    r'[A-Za-z_]\w*'
    if t.value in RESERVED_WORDS:
        t.type = t.value.upper()
    elif t.value in VAR_NAMES:
        t.type = 'VAR'
    elif t.value in FUNC_NAMES:
        t.type = 'FUNC'
    else:
        t_error(t)
    return t


def t_error(t):
    print("LEX: ILLEGAL CHARACTER '%s'" % t.value[0])
    t.lexer.skip(1)

# ===============================================================================
#
#                               LEXEMS MAIN FUNCTION
#
# ===============================================================================


if __name__ == "__main__":
    import sys
    PROG = open(sys.argv[1]).read()

    LEX.input(PROG)

    while 1:
        TOKEN = LEX.token()
        if not TOKEN:
            break
        print("LINE %d %s(%s)" % (TOKEN.lineno, TOKEN.TYPE, TOKEN.value))
