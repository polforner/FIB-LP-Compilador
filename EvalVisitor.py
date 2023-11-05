if __name__ is not None and "." in __name__:
    from .funxParser import funxParser
    from .funxVisitor import funxVisitor
else:
    from funxParser import funxParser
    from funxVisitor import funxVisitor

d = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
     '*': lambda x, y: x * y, '/': lambda x, y: x // y,
     '^': lambda x, y: x ** y, '%': lambda x, y: x % y,
     '=': lambda x, y: x == y, '!=': lambda x, y: x != y,
     '<': lambda x, y: x < y, '>': lambda x, y: x > y, '<=': lambda x, y: x <= y, '>=': lambda x, y: x >= y}


class EvalVisitor(funxVisitor):

    def __init__(self, ts, tfs):
        self.ts = ts
        self.tfs = tfs

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0])

    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        variable = l[0].getText()
        valor = self.visit(l[2])
        self.ts[-1][variable] = valor

    def visitIfElse(self, ctx):
        l = list(ctx.getChildren())
        condicion = self.visit(l[1])
        if condicion:
            return self.visit(l[2])
        elif len(l) == 5:
            return self.visit(l[4])

    def visitWhile(self, ctx):
        l = list(ctx.getChildren())
        while self.visit(l[1]):
            result = self.visit(l[2])
            if result != None:
                return result

    def visitDeclaracionFunc(self, ctx):
        l = list(ctx.getChildren())
        nomFunc = l[0].getText()
        if nomFunc in self.tfs:
            raise Exception('La funcion ' + nomFunc + ' ya ha sido declarada!')
        else:
            i = 1
            parametres = []
            while i < len(l) - 1:
                parametres += l[i].getText()
                i += 1
            self.tfs[nomFunc] = (parametres, l[-1])
            return None

    def visitLlamadaFunc(self, ctx):
        l = list(ctx.getChildren())
        nomFunc = l[0].getText()
        if not (nomFunc in self.tfs):
            raise Exception('Funcion no declarada!')
        elif len(l) - 1 != len(self.tfs[nomFunc][0]):
            raise Exception('Numero de parametres incorrectes!')
        else:
            i = 1
            ts = {}
            while i < len(l):
                nomVar = self.tfs[nomFunc][0][i - 1]
                valorVar = self.visit(l[i])
                ts[nomVar] = valorVar
                i += 1
            self.ts.append(ts)
            result = self.visit(self.tfs[nomFunc][1])
            del self.ts[-1]
            return result

    def visitBloque(self, ctx):
        l = list(ctx.getChildren())
        i = 1
        while i < len(l) - 1:
            result = self.visit(l[i])
            if result != None:
                return result
            i += 1

    def visitBoolexpr(self, ctx):
        l = list(ctx.getChildren())
        op = l[1].getText()
        x = self.visit(l[0])
        y = self.visit(l[2])
        return (d[op])(x, y)

    def visitPar(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1])

    def visitBin(self, ctx):
        l = list(ctx.getChildren())
        op = l[1].getText()
        x = self.visit(l[0])
        y = self.visit(l[2])
        if (op == '/' and y == 0):
            raise Exception("Divisio per zero!")
        else:
            return (d[op])(x, y)

    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    def visitVariable(self, ctx):
        l = list(ctx.getChildren())
        nomVar = l[0].getText()
        for dir in reversed(self.ts):
            if nomVar in dir:
                return dir[nomVar]
        self.ts[-1][nomVar] = 0
        return self.ts[-1][nomVar]
