
from dataclasses import dataclass

import lexer_token as token
from lexer_token import Token, TokenType


@dataclass
class Lexer:
    input: str
    position: int = 0
    read_position: int = 0
    ch: str = '' # Current character

    def readChar(self) -> None:
        if self.read_position >= len(self.input):
            self.ch = ''
        else:
            self.ch = self.input[self.read_position]

        self.position = self.read_position
        self. read_position += 1

    def nextToken(self) -> Token:
        tok: Token

        self.skipWhitespace()

        match self.ch:
            case '=':
                if self.peekChar() == '=':
                    tok = Token(token.EQ, '==')
                    self.readChar()
                else:
                    tok = Token(token.ASSIGN, '=')
            case '+':
                tok = Token(token.PLUS, '+')
            case '-':
                tok = Token(token.MINUS, '-')
            case '!':
                if self.peekChar() == '=':
                    tok = Token(token.NOT_EQ, '!=')
                    self.readChar()
                else:
                    tok = Token(token.BANG, '!')
            case '*':
                tok = Token(token.ASTERISK, '*')
            case '/':
                tok = Token(token.SLASH, '/')
            case '<':
                tok = Token(token.LT, '<')
            case '>':
                tok = Token(token.GT, '>')
            case ',':
                tok = Token(token.GT, ',')
            case ';':
                tok = Token(token.SEMICOLON, ';')
            case '(':
                tok = Token(token.LPAREN, '(')
            case ')':
                tok = Token(token.RPAREN, ')')
            case '{':
                tok = Token(token.LBRACE, '{')
            case '}':
                tok = Token(token.RBRACE, '}')
            case '':
                tok = Token(token.EOF, '')
            case _:
                if self.ch.isdigit():
                    tok = Token(token.INT, self.readDigit())
                elif self.ch.isalpha():
                    tok = Token(token.IDENT, self.readIdentifier())
                    tok.type = tok.lookupIdent()
                    print(tok.literal)
                else:
                    tok = Token(token.ILLEGAL, self.ch)

        return tok

    def peekChar(self) -> str:
        if self.read_position >= len(self.input):
            return ''
        else:
            return self.input[self.read_position]

    def readDigit(self) -> str:
        digit: str = self.ch
        while self.peekChar().isdigit():
            digit += self.peekChar()
            self.readChar()
        return digit

    def readIdentifier(self) -> str:
        identifier: str = self.ch
        while self.peekChar().isalpha():
            identifier += self.peekChar()
            self.readChar()
        return identifier

    def skipWhitespace(self) -> None:
        if self.ch == ' ':
            self.readChar()


if __name__ == "__main__":
    lexer = Lexer("if")

    for i in range(len(lexer.input)):
        lexer.readChar()
        print(lexer.nextToken())

