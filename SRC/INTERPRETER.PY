import AST
from AST import addToClass
from functools import reduce

__author__ = "GABRIEL FREITAS, QUENTIN JEANMONOD"

operations = {
    'PLUS': lambda X, Y: X + Y,
    'MINUS': lambda X, Y: X - Y,
    'BY': lambda X, Y: X * Y,
    'OUT OF': lambda X, Y: X / Y
}

VARS = {}
FUNCS = {}


@addToClass(AST.ProgramNode)
def execute(self):
    for c in self.children:
        if c.type == 'RETURN':
            return c.execute()
        c.execute()


@addToClass(AST.DeclareFunctionNode)
def execute(self):
    FUNCS[self.name] = self


@addToClass(AST.FunctionNode)
def execute(self):
    try:
        SAVEVARS = {i: j for i, j in VARS.items()}
        VARS.clear()
        for i, j in zip(FUNCS[self.name].params.children, self.params.children):
            VARS[i.tok] = {None: j.execute()}
        for c in FUNCS[self.name].children:
            if c.type == 'RETURN':
                OUT = c.execute()
                VARS.clear()
                VARS.update(SAVEVARS)
                return OUT
            c.execute()
        VARS.clear()
        VARS.update(SAVEVARS)
    except KeyError:
        print("*** ERROR: FUNC {} NOT DEFINED!".format(self.name))


@addToClass(AST.ReturnNode)
def execute(self):
    return VARS[self.children[0].tok]


@addToClass(AST.TokenNode)
def execute(self):
    if isinstance(self.tok, str):
        try:
            return VARS[self.tok][self.accessor]
        except KeyError:
            print("*** ERROR: VAR {}.{} NOT DEFINED!".format(self.tok, self.accessor))
    return self.tok


@addToClass(AST.OpNode)
def execute(self):
    ARGS = [c.execute() for c in self.children]
    if len(ARGS) == 1:
        ARGS.insert(0, 0)
    return reduce(operations[self.op], ARGS)


@addToClass(AST.AssignNode)
def execute(self):
    if self.children[0].tok not in VARS:
        VARS[self.children[0].tok] = dict()
    VALUE = self.children[1].execute()
    if isinstance(VALUE, dict):
        VARS[self.children[0].tok].update(VALUE)
    else:
        VARS[self.children[0].tok][self.children[0].accessor] = VALUE


@addToClass(AST.PrintNode)
def execute(self):
    VALUE = self.children[0].execute()
    if self.text:
        print(chr(VALUE), end='')
    else:
        if isinstance(VALUE, bool):
            VALUE = 'YEA' if VALUE else 'NAY'
        print(VALUE, end='')


@addToClass(AST.WhileNode)
def execute(self):
    while self.children[0].execute():
        self.children[1].execute()


if __name__ == '__main__':
    from PARSER import PARSE
    import sys
    PROG = open(sys.argv[1]).read()
    AST = PARSE(PROG)

    AST.execute()
