# Generated from traductorPyaJava.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("O\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\7\r?\n\r\f\r\16\rB")
        buf.write("\13\r\3\16\6\16E\n\16\r\16\16\16F\3\17\6\17J\n\17\r\17")
        buf.write("\16\17K\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2\6\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2Q\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\3\37\3\2\2\2\5#\3\2\2\2\7*\3\2\2\2\t,\3\2")
        buf.write("\2\2\13.\3\2\2\2\r\60\3\2\2\2\17\62\3\2\2\2\21\64\3\2")
        buf.write("\2\2\23\66\3\2\2\2\258\3\2\2\2\27:\3\2\2\2\31<\3\2\2\2")
        buf.write("\33D\3\2\2\2\35I\3\2\2\2\37 \7f\2\2 !\7g\2\2!\"\7h\2\2")
        buf.write("\"\4\3\2\2\2#$\7t\2\2$%\7g\2\2%&\7v\2\2&\'\7w\2\2\'(\7")
        buf.write("t\2\2()\7p\2\2)\6\3\2\2\2*+\7*\2\2+\b\3\2\2\2,-\7+\2\2")
        buf.write("-\n\3\2\2\2./\7.\2\2/\f\3\2\2\2\60\61\7<\2\2\61\16\3\2")
        buf.write("\2\2\62\63\7?\2\2\63\20\3\2\2\2\64\65\7-\2\2\65\22\3\2")
        buf.write("\2\2\66\67\7/\2\2\67\24\3\2\2\289\7,\2\29\26\3\2\2\2:")
        buf.write(";\7\61\2\2;\30\3\2\2\2<@\t\2\2\2=?\t\3\2\2>=\3\2\2\2?")
        buf.write("B\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\32\3\2\2\2B@\3\2\2\2CE")
        buf.write("\t\4\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\34\3")
        buf.write("\2\2\2HJ\t\5\2\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2")
        buf.write("\2LM\3\2\2\2MN\b\17\2\2N\36\3\2\2\2\6\2@FK\3\b\2\2")
        return buf.getvalue()


class traductorPyaJavaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEF = 1
    RETURN = 2
    LPAREN = 3
    RPAREN = 4
    COMMA = 5
    COLON = 6
    ASSIGN = 7
    PLUS = 8
    MINUS = 9
    MULTIPLY = 10
    DIVIDE = 11
    ID = 12
    Number = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'return'", "'('", "')'", "','", "':'", "'='", "'+'", 
            "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "RETURN", "LPAREN", "RPAREN", "COMMA", "COLON", "ASSIGN", 
            "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "ID", "Number", "WS" ]

    ruleNames = [ "DEF", "RETURN", "LPAREN", "RPAREN", "COMMA", "COLON", 
                  "ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "ID", 
                  "Number", "WS" ]

    grammarFileName = "traductorPyaJava.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


