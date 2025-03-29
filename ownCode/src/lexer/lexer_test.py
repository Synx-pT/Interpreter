import pytest

from lexer import ...

def test_single_identifier():
    input_str = "foobar"
    tokens = lex(input_str)
    expected_tokens = [
        Token(TokenType.IDENT, "foobar"),
        Token(TokenType.EOF, "")
    ]
    assert tokens == expected_tokens

def test_keyword_recognition():
    input_str = "if"
    tokens = lex(input_str)
    expected_tokens = [
        Token(TokenType.IF, "if"),
        Token(TokenType.EOF, "")
    ]
    assert tokens == expected_tokens

def test_multiple_tokens():
    input_str = "if foo else"
    tokens = lex(input_str)
    expected_tokens = [
        Token(TokenType.IF, "if"),
        Token(TokenType.IDENT, "foo"),
        Token(TokenType.ELSE, "else"),
        Token(TokenType.EOF, "")
    ]
    assert tokens == expected_tokens
