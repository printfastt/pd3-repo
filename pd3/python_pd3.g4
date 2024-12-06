grammar python_pd3;

tokens { INDENT, DEDENT }

@lexer::members {
import sys
from antlr4 import Lexer
from antlr4.Token import CommonToken
from antlr4.Token import Token

class CustomLexer(Lexer):
    def __init__(self, input=None, output=sys.stdout):
        super().__init__(input, output)
        self.indentStack = [0]
        self.bufferedTokens = []

    def emitToken(self, t):
        self.setToken(t)
        return t

    def nextToken(self):
        if self.bufferedTokens:
            return self.bufferedTokens.pop(0)

        token = super().nextToken()
        if token.type == Token.EOF:
            while len(self.indentStack) > 1:
                self.indentStack.pop()
                dedent = CommonToken(token)
                dedent.type = self.DEDENT
                dedent.text = ""
                self.bufferedTokens.append(dedent)
            if self.bufferedTokens:
                return self.bufferedTokens.pop(0)
            return token

        if token.type == self.NEWLINE:
            spacesCount = 0
            tabsCount = 0
            pos = 1
            while True:
                c = self._input.LA(pos)
                if c == ord(' '):
                    spacesCount += 1
                elif c == ord('\t'):
                    tabsCount += 1
                else:
                    break
                pos += 1

            newIndent = spacesCount + tabsCount*4
            currentIndent = self.indentStack[-1]

            newlineToken = CommonToken(token)
            newlineToken.type = self.NEWLINE
            newlineToken.text = token.text
            self.bufferedTokens.append(newlineToken)

            if newIndent > currentIndent:
                self.indentStack.append(newIndent)
                indent = CommonToken(token)
                indent.type = self.INDENT
                indent.text = ""
                self.bufferedTokens.append(indent)
            elif newIndent < currentIndent:
                while len(self.indentStack) > 1 and self.indentStack[-1] > newIndent:
                    self.indentStack.pop()
                    dedent = CommonToken(token)
                    dedent.type = self.DEDENT
                    dedent.text = ""
                    self.bufferedTokens.append(dedent)

            for i in range(spacesCount + tabsCount):
                self._input.consume()

            return self.bufferedTokens.pop(0)

        return token
}

program: (statement | NEWLINE)*;

statement
    : assignment
    | if_block
    | while_loop
    | for_loop
    ;

assignment
    : VARIABLE ASSIGN expression
    | VARIABLE ADD_ASSIGN expression
    | VARIABLE SUB_ASSIGN expression
    | VARIABLE MUL_ASSIGN expression
    | VARIABLE DIV_ASSIGN expression
    ;

if_block
    : IF condition COLON NEWLINE block (elif_clause)* (else_clause)?
    ;

elif_clause
    : ELIF condition COLON NEWLINE block
    ;

else_clause
    : ELSE COLON NEWLINE block
    ;

while_loop
    : WHILE condition COLON NEWLINE block
    ;

for_loop
    : FOR VARIABLE IN iterable COLON NEWLINE block
    ;

block
    : INDENT statement+ DEDENT
    ;

expression
    : expression ADD expression
    | expression SUB expression
    | expression MUL expression
    | expression DIV expression
    | expression MOD expression
    | '(' expression ')'
    | list
    | STRING
    | NUMBER
    | VARIABLE
    ;

condition
    : expression comparison expression
    | NOT condition
    | condition AND condition
    | condition OR condition
    ;

list
    : '[' expression (',' expression)* ']'
    ;

iterable
    : list
    | RANGE '(' expression (',' expression)? ')'
    ;

comparison
    : LESS
    | LESSEQ
    | GRTR
    | GRTREQ
    | EQL
    | NEQL
    ;

LESS       : '<';
LESSEQ     : '<=';
GRTR       : '>';
GRTREQ     : '>=';
EQL        : '==';
NEQL        : '!=';
ADD        : '+';
SUB        : '-';
MUL        : '*';
DIV        : '/';
MOD        : '%';
AND        : 'and';
OR         : 'or';
NOT        : 'not';
IF         : 'if';
ELIF       : 'elif';
ELSE       : 'else';
WHILE      : 'while';
FOR        : 'for';
IN         : 'in';
RANGE      : 'range';
VARIABLE   : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER     : [0-9]+ ('.' [0-9]+)?;
STRING     : '"' .*? '"' | '\'' .*? '\'';
COMMENT    : '#' ~[\r\n]* -> skip;
MULTI_COMMENT: '"""' .*? '"""' -> skip;
COMMA      : ',';
COLON      : ':';
NEWLINE    : [\r\n]+;
ASSIGN     : '=';
ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MUL_ASSIGN : '*=';
DIV_ASSIGN : '/=';
WS: [ \t]+ -> skip;
