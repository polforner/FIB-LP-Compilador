# Generated from funx.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,3,0,20,8,0,1,0,1,0,1,1,1,1,5,1,26,
        8,1,10,1,12,1,29,9,1,1,1,1,1,1,2,1,2,4,2,35,8,2,11,2,12,2,36,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,50,8,3,1,3,1,3,1,3,1,
        3,3,3,56,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,69,
        8,5,10,5,12,5,72,9,5,1,5,1,5,3,5,76,8,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,5,5,87,8,5,10,5,12,5,90,9,5,1,5,0,1,10,6,0,2,4,6,8,10,
        0,3,1,0,7,12,1,0,16,18,2,0,19,19,23,23,100,0,15,1,0,0,0,2,23,1,0,
        0,0,4,32,1,0,0,0,6,55,1,0,0,0,8,57,1,0,0,0,10,75,1,0,0,0,12,14,3,
        2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,
        19,1,0,0,0,17,15,1,0,0,0,18,20,3,10,5,0,19,18,1,0,0,0,19,20,1,0,
        0,0,20,21,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,27,5,20,0,0,24,26,
        3,10,5,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,
        28,30,1,0,0,0,29,27,1,0,0,0,30,31,3,4,2,0,31,3,1,0,0,0,32,34,5,1,
        0,0,33,35,3,6,3,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,
        1,0,0,0,37,38,1,0,0,0,38,39,5,2,0,0,39,5,1,0,0,0,40,56,3,10,5,0,
        41,42,5,21,0,0,42,43,5,3,0,0,43,56,3,10,5,0,44,45,5,4,0,0,45,46,
        3,8,4,0,46,49,3,4,2,0,47,48,5,5,0,0,48,50,3,4,2,0,49,47,1,0,0,0,
        49,50,1,0,0,0,50,56,1,0,0,0,51,52,5,6,0,0,52,53,3,8,4,0,53,54,3,
        4,2,0,54,56,1,0,0,0,55,40,1,0,0,0,55,41,1,0,0,0,55,44,1,0,0,0,55,
        51,1,0,0,0,56,7,1,0,0,0,57,58,3,10,5,0,58,59,7,0,0,0,59,60,3,10,
        5,0,60,9,1,0,0,0,61,62,6,5,-1,0,62,63,5,13,0,0,63,64,3,10,5,0,64,
        65,5,14,0,0,65,76,1,0,0,0,66,70,5,20,0,0,67,69,3,10,5,0,68,67,1,
        0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,76,1,0,0,0,72,
        70,1,0,0,0,73,76,5,22,0,0,74,76,5,21,0,0,75,61,1,0,0,0,75,66,1,0,
        0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,88,1,0,0,0,77,78,10,6,0,0,78,
        79,5,15,0,0,79,87,3,10,5,6,80,81,10,5,0,0,81,82,7,1,0,0,82,87,3,
        10,5,6,83,84,10,4,0,0,84,85,7,2,0,0,85,87,3,10,5,5,86,77,1,0,0,0,
        86,80,1,0,0,0,86,83,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,
        0,0,0,89,11,1,0,0,0,90,88,1,0,0,0,10,15,19,27,36,49,55,70,75,86,
        88
    ]

class funxParser ( Parser ):

    grammarFileName = "funx.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'<-'", "'if'", "'else'", 
                     "'while'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'('", "')'", "'^'", "'*'", "'/'", "'%'", "'-'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "FUNC", "ID", "NUM", "MES", "COMENT", "WS" ]

    RULE_root = 0
    RULE_func = 1
    RULE_bloque = 2
    RULE_stat = 3
    RULE_boolexpr = 4
    RULE_expr = 5

    ruleNames =  [ "root", "func", "bloque", "stat", "boolexpr", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    FUNC=20
    ID=21
    NUM=22
    MES=23
    COMENT=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(funxParser.EOF, 0)

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.FuncContext)
            else:
                return self.getTypedRuleContext(funxParser.FuncContext,i)


        def expr(self):
            return self.getTypedRuleContext(funxParser.ExprContext,0)


        def getRuleIndex(self):
            return funxParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = funxParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 12
                    self.func() 
                self.state = 17
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 7348224) != 0:
                self.state = 18
                self.expr(0)


            self.state = 21
            self.match(funxParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return funxParser.RULE_func

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclaracionFuncContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNC(self):
            return self.getToken(funxParser.FUNC, 0)
        def bloque(self):
            return self.getTypedRuleContext(funxParser.BloqueContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.ExprContext)
            else:
                return self.getTypedRuleContext(funxParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionFunc" ):
                return visitor.visitDeclaracionFunc(self)
            else:
                return visitor.visitChildren(self)



    def func(self):

        localctx = funxParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        self._la = 0 # Token type
        try:
            localctx = funxParser.DeclaracionFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(funxParser.FUNC)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 7348224) != 0:
                self.state = 24
                self.expr(0)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.StatContext)
            else:
                return self.getTypedRuleContext(funxParser.StatContext,i)


        def getRuleIndex(self):
            return funxParser.RULE_bloque

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = funxParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(funxParser.T__0)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                self.stat()
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 7348304) != 0):
                    break

            self.state = 38
            self.match(funxParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return funxParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssigContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(funxParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(funxParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)


    class IfElseContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolexpr(self):
            return self.getTypedRuleContext(funxParser.BoolexprContext,0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.BloqueContext)
            else:
                return self.getTypedRuleContext(funxParser.BloqueContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionsContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(funxParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions" ):
                return visitor.visitExpressions(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolexpr(self):
            return self.getTypedRuleContext(funxParser.BoolexprContext,0)

        def bloque(self):
            return self.getTypedRuleContext(funxParser.BloqueContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = funxParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = funxParser.ExpressionsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = funxParser.AssigContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(funxParser.ID)
                self.state = 42
                self.match(funxParser.T__2)
                self.state = 43
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = funxParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.match(funxParser.T__3)
                self.state = 45
                self.boolexpr()
                self.state = 46
                self.bloque()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 47
                    self.match(funxParser.T__4)
                    self.state = 48
                    self.bloque()


                pass

            elif la_ == 4:
                localctx = funxParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.match(funxParser.T__5)
                self.state = 52
                self.boolexpr()
                self.state = 53
                self.bloque()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.ExprContext)
            else:
                return self.getTypedRuleContext(funxParser.ExprContext,i)


        def getRuleIndex(self):
            return funxParser.RULE_boolexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolexpr" ):
                return visitor.visitBoolexpr(self)
            else:
                return visitor.visitChildren(self)




    def boolexpr(self):

        localctx = funxParser.BoolexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_boolexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.expr(0)
            self.state = 58
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 59
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return funxParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(funxParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar" ):
                return visitor.visitPar(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(funxParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class BinContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.ExprContext)
            else:
                return self.getTypedRuleContext(funxParser.ExprContext,i)

        def MES(self):
            return self.getToken(funxParser.MES, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBin" ):
                return visitor.visitBin(self)
            else:
                return visitor.visitChildren(self)


    class ValorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(funxParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)


    class LlamadaFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNC(self):
            return self.getToken(funxParser.FUNC, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.ExprContext)
            else:
                return self.getTypedRuleContext(funxParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFunc" ):
                return visitor.visitLlamadaFunc(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = funxParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = funxParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 62
                self.match(funxParser.T__12)
                self.state = 63
                self.expr(0)
                self.state = 64
                self.match(funxParser.T__13)
                pass
            elif token in [20]:
                localctx = funxParser.LlamadaFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(funxParser.FUNC)
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 67
                        self.expr(0) 
                    self.state = 72
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass
            elif token in [22]:
                localctx = funxParser.ValorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 73
                self.match(funxParser.NUM)
                pass
            elif token in [21]:
                localctx = funxParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                self.match(funxParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 86
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = funxParser.BinContext(self, funxParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 78
                        self.match(funxParser.T__14)
                        self.state = 79
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = funxParser.BinContext(self, funxParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 81
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 82
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = funxParser.BinContext(self, funxParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 84
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 85
                        self.expr(5)
                        pass

             
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




