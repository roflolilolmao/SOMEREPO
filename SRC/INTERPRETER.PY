import AST
from AST import *
from functools import reduce

__author__ = "GABRIEL FREITAS, QUENTIN JEANMONOD"

operations = {
    'PLUS': lambda X, Y: X + Y,
    'MINUS': lambda X, Y: X - Y,
    'BY': lambda X, Y: X * Y,
    'OUT OF': lambda X, Y: X / Y,
    'OR': lambda X, Y: X or Y,
    'AND': lambda X, Y: X and Y
}

compare_operations = {
    'GREATER THAN': lambda X, Y: X > Y,
    'SMALLER THAN': lambda X, Y: X < Y,
    'EQUAL TO': lambda X, Y: X == Y
}

ORDERED = "ORDERED"

VARS = {}
FUNCS = {}


@addToClass(AST.ProgramNode)
def execute(self):
    for c in self.children:
        OUT = c.execute()
        if OUT:
            return OUT


@addToClass(AST.DeclareFunctionNode)
def execute(self):
    FUNCS[self.name] = self


@addToClass(AST.FunctionNode)
def execute(self):
    try:
        SAVEVARS = {i: j for i, j in VARS.items()}
        NEWVARS = {}
        for i, j in zip(FUNCS[self.name].children[0].children, self.children[0].children):
            NEWVARS[i.tok] = {None: j.execute()}
        VARS.clear()
        VARS.update(NEWVARS)
        for c in FUNCS[self.name].children[1].children:
            OUT = c.execute()
            if OUT:
                VARS.clear()
                VARS.update(SAVEVARS)
                return OUT
        VARS.clear()
        VARS.update(SAVEVARS)
    except KeyError:
        print("*** ERROR: FUNC {} NOT DEFINED!".format(self.name))
        print(self.name)
        print(FUNCS)


@addToClass(AST.ReturnNode)
def execute(self):
    try:
        return VARS[self.children[0].tok]
    except:
        return self.children[0].execute()


@addToClass(AST.ExistenceNode)
def execute(self):
    value = self.children[0].execute()
    for key in VARS[self.children[1]]:
        if value == VARS[self.children[1]][key]:
            return True
    return False


@addToClass(AST.TokenNode)
def execute(self):
    if isinstance(self.tok, str):
        try:
            return VARS[self.tok][self.accessor]
        except KeyError:
            print("*** ERROR: VAR {}.{} NOT DEFINED!".format(self.tok, self.accessor))
            print(VARS, FUNCS)
            print('\n')
    return self.tok


@addToClass(AST.CompareNode)
def execute(self):
    return reduce(compare_operations[self.op], [c.execute() for c in self.children])


@addToClass(AST.NotNode)
def execute(self):
    return not self.children[0].execute()


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
        VARS[self.children[0].tok][ORDERED] = list()

    if self.children[1].type == "PARAMS":
        VALUE = [c.execute() for c in self.children[1].children]
    else:
        VALUE = self.children[1].execute()

    if isinstance(VALUE, dict):
        VARS[self.children[0].tok].update(VALUE)
    elif isinstance(VALUE, list):
        VARS[self.children[0].tok][ORDERED] = VALUE
    else:
        VARS[self.children[0].tok][self.children[0].accessor] = VALUE


@addToClass(AST.ListNode)
def execute(self):
    if len(self.children) == 1:
        return VARS[self.children[0]][ORDERED]
    return VARS[self.children[0]][ORDERED][self.children[1].execute()]


@addToClass(AST.AsciiNode)
def execute(self):
    return chr(self.children[0].execute())


@addToClass(AST.PrintNode)
def execute(self):

    VALUE = self.children[0].execute()

    if isinstance(VALUE, dict):
        VALUE = VALUE[None]
    if isinstance(VALUE, bool):
        VALUE = 'YEA' if VALUE else 'NAY'

    print(VALUE, end='')


@addToClass(AST.WhileNode)
def execute(self):
    while self.children[0].execute():
        self.children[1].execute()


@addToClass(AST.MapNode)
def execute(self):
    for c in VARS[self.children[0]].keys():
        self.children[1].children[0] = ParamsNode([TokenNode(self.children[0], c)] + self.children[2].children)
        OUT = self.children[1].execute()
        if OUT:
            VARS[self.children[0]][c] = OUT


@addToClass(AST.SomehowNode)
def execute(self):
    if self.children[0].execute():
        return self.children[1].execute()
    else:
        return self.children[2].execute()


if __name__ == '__main__':
    from PARSER import PARSE
    import sys

    with open(sys.argv[1]) as PROG:
        AST = PARSE(PROG.read())
    AST.execute()
