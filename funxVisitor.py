# Generated from funx.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .funxParser import funxParser
else:
    from funxParser import funxParser

# This class defines a complete generic visitor for a parse tree produced by funxParser.

class funxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by funxParser#root.
    def visitRoot(self, ctx:funxParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#DeclaracionFunc.
    def visitDeclaracionFunc(self, ctx:funxParser.DeclaracionFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#bloque.
    def visitBloque(self, ctx:funxParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Expressions.
    def visitExpressions(self, ctx:funxParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Assig.
    def visitAssig(self, ctx:funxParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#IfElse.
    def visitIfElse(self, ctx:funxParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#While.
    def visitWhile(self, ctx:funxParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#boolexpr.
    def visitBoolexpr(self, ctx:funxParser.BoolexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Par.
    def visitPar(self, ctx:funxParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Variable.
    def visitVariable(self, ctx:funxParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Bin.
    def visitBin(self, ctx:funxParser.BinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Valor.
    def visitValor(self, ctx:funxParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#LlamadaFunc.
    def visitLlamadaFunc(self, ctx:funxParser.LlamadaFuncContext):
        return self.visitChildren(ctx)



del funxParser