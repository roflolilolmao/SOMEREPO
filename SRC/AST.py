# coding: latin-1

""" Petit module utilitaire pour la construction, la manipulation et la
repr�sentation d'arbres syntaxiques abstraits.

S�rement plein de bugs et autres surprises. � prendre comme un
"work in progress"...
Notamment, l'utilisation de pydot pour repr�senter un arbre syntaxique cousu
est une utilisation un peu "limite" de graphviz. �a marche, mais le layout n'est
pas toujours optimal...
"""


class Node:
    count = 0
    type = 'Node (unspecified)'
    shape = 'ellipse'

    def __init__(self, children=None):
        self.ID = str(Node.count)
        Node.count += 1
        if not children:
            self.children = []
        elif hasattr(children, '__len__'):
            self.children = children
        else:
            self.children = [children]
        self.next = []

    def addNext(self, nextNode):
        self.next.append(nextNode)

    def asciitree(self, prefix=''):
        result = "%s%s\n" % (prefix, repr(self))
        prefix += '|  '
        for c in self.children:
            if not isinstance(c, Node):
                result += "%s*** Error: Child of type %r: %r\n" % (prefix, type(c), c)
                continue
            result += c.asciitree(prefix)
        return result
    
    def __str__(self):
        return self.asciitree()
    
    def __repr__(self):
        return self.type


class ProgramNode(Node):
    type = 'PROGRAM'


class DeclareFunctionNode(Node):
    type = 'DECLFUNCTION'

    def __init__(self, name, children):
        Node.__init__(self, children)
        self.name = name

    def __repr__(self):
        return 'DECLARE {}'.format(self.name)


class FunctionNode(Node):
    type = 'FUNCTION'

    def __init__(self, name, children):
        Node.__init__(self, children)
        self.name = name

    def __repr__(self):
        return 'FUNC {}'.format(self.name)


class ParamsNode(Node):
    type = 'PARAMS'


class MapNode(Node):
    type = 'MAP'

    def __init__(self, children, ordered=False):
        Node.__init__(self, children)
        self.ordered = ordered

    def __repr__(self):
        return 'MAP {} {}'.format(self.children[0], self.children[1])


class ListNode(Node):
    type = "LIST"

    def __init__(self, children):
        Node.__init__(self, children)

    def __repr__(self):
        return "LIST : {}".format(self.children[0])


class TokenNode(Node):
    type = 'TOKEN'

    def __init__(self, tok, accessor=None):
        Node.__init__(self)
        self.tok = tok
        self.accessor = accessor

    def __repr__(self):
        return '{}.{}'.format(self.tok, self.accessor)


class OpNode(Node):
    def __init__(self, op, children):
        Node.__init__(self, children)
        self.op = op
        try:
            self.nbargs = len(children)
        except AttributeError:
            self.nbargs = 1
        
    def __repr__(self):
        return "{} ({})".format(self.op, self.nbargs)


class CompareNode(Node):
    type = "COMPARE"

    def __init__(self, op, children):
        Node.__init__(self, children)
        self.op = op

    def __repr__(self):
        return '{}'.format(self.op)


class ExistenceNode(Node):
    type = "EXISTENCE"

    def __init__(self, value, var):
        Node.__init__(self, [value, var])

    def __repr__(self):
        return "ExistenceNode : {}".format(self.children)


class SomehowNode(Node):
    type = 'SOMEHOW'


class AssignNode(Node):
    type = 'IS'


class ReturnNode(Node):
    type = 'GIVE ME'


class AsciiNode(Node):
    type = 'ASCII'


class PrintNode(Node):
    type = 'SHOW ME'


class WhileNode(Node):
    type = 'while'


class NotNode(Node):
    type = 'while'


def addToClass(cls):
    """ D�corateur permettant d'ajouter la fonction d�cor�e en tant que m�thode
    � une classe.

    Permet d'impl�menter une forme �l�mentaire de programmation orient�e
    aspects en regroupant les m�thodes de diff�rentes classes impl�mentant
    une m�me fonctionnalit� en un seul endroit.

    Attention, apr�s utilisation de ce d�corateur, la fonction d�cor�e reste dans
    le namespace courant. Si cela d�range, on peut utiliser del pour la d�truire.
    Je ne sais pas s'il existe un moyen d'�viter ce ph�nom�ne.
    """
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator
