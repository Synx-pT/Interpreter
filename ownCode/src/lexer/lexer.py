
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

        match self.ch:
            case '=':
                tok = Token(token.ASSIGN, '=')
            case ';':
                tok = Token(token.SEMICOLON, ';')
            case '':
                tok = Token(token.EOF, '')
            case _:
                tok = Token(token.ILLEGAL, self.ch)

        return tok

