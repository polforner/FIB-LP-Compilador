if __name__ is not None and "." in __name__:
    from .funxParser import funxParser
    from .funxVisitor import funxVisitor
else:
    from funxParser import funxParser
    from funxVisitor import funxVisitor
    
class TreeVisitor(funxVisitor):
    def __init__(self):
        self.nivell = 0
    def visitPar(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + l[0].getText())
        self.nivell += 1
        self.visit(l[1])
        self.nivell -= 1
        print('  ' *  self.nivell + l[2].getText())
    def visitBin(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + l[1].getText())
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1
    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        print("  " * self.nivell +
              funxParser.symbolicNames[l[0].getSymbol().type] +
              '(' +l[0].getText() + ')')
