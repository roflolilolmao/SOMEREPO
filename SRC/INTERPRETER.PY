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
    FUNCS[self.name] = self.children


@addToClass(AST.FunctionNode)
def execute(self):
    try:
        for c in FUNCS[self.name]:
            if c.type == 'RETURN':
                return c.execute()
            c.execute()
    except KeyError:
        print("*** ERROR: FUNC {} NOT DEFINED!".format(self.name))


@addToClass(AST.ReturnNode)
def execute(self):
    return self.children[0].execute()


@addToClass(AST.TokenNode)
def execute(self):
    if isinstance(self.tok, str):
        try:
            return VARS[self.tok]
        except KeyError:
            print("*** ERROR: VAR {} NOT DEFINED!".format(self.tok))
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
    if len(self.children) == 3:
        VARS[self.children[0].tok][self.children[1].tok] = self.children[2].execute()
    else:
        VARS[self.children[0].tok][None] = self.children[1].execute()


@addToClass(AST.PrintNode)
def execute(self):
    if len(self.children) > 1:
        print(self.children[0].execute()[self.children[1].execute()])
    else:
        print(self.children[0].execute()[None])


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
