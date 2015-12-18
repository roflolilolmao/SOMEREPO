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


@addToClass(AST.ProgramNode)
def execute(self):
    for c in self.children:
        c.execute()


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
    VARS[self.children[0].tok] = self.children[1].execute()


@addToClass(AST.PrintNode)
def execute(self):
    print(self.children[0].execute())


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
