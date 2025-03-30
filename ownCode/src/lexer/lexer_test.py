import pytest

from lexer import *
from lexer import Lexer

def test_single_identifier():

    lexer = Lexer("=;🥺")

    expected_tokens = [
        Token(token.ASSIGN, "="),
        Token(token.SEMICOLON, ";"),
        Token(token.ILLEGAL, "🥺"),
        Token(token.EOF, "")
    ]

    for i in range(len(expected_tokens)):
        lexer.readChar()
        tok = lexer.nextToken()
        assert tok == expected_tokens[i], f"Expected {expected_tokens[i]}, but got {tok}"


if __name__ == "__main__":
    test_single_identifier()
