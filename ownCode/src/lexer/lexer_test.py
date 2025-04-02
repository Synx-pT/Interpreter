
from lexer import *
from lexer import Lexer

def test_single_operator():

    lexer = Lexer("=")

    expected_tokens = [
        Token(token.ASSIGN, "="),
        Token(token.EOF, "")
    ]

    for i in range(len(expected_tokens)):
        lexer.readChar()
        tok = lexer.nextToken()
        assert tok == expected_tokens[i], f"Expected {expected_tokens[i]}, but got {tok}"


def test_multiple_operator():

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


def test_2_digit_operator():

    lexer = Lexer("==")

    expected_tokens = [
        Token(token.EQ, "=="),
        Token(token.EOF, "")
    ]

    for i in range(len(expected_tokens)):
        lexer.readChar()
        tok = lexer.nextToken()
        assert tok == expected_tokens[i], f"Expected {expected_tokens[i]}, but got {tok}"


def test_literal_and_number():

    lexer = Lexer("=12ab")

    expected_tokens = [
        Token(token.ASSIGN, "="),
        Token(token.INT, "12"),
        Token(token.IDENT, "ab"),
        Token(token.EOF, "")
    ]

    for i in range(len(expected_tokens)):
        lexer.readChar()
        tok = lexer.nextToken()
        assert tok == expected_tokens[i], f"Expected {expected_tokens[i]}, but got {tok}"


def test_keyword():

    lexer = Lexer("if")

    expected_tokens = [
        Token(token.IF, "if"),
        Token(token.EOF, "")
    ]

    for i in range(len(expected_tokens)):
        lexer.readChar()
        tok = lexer.nextToken()
        assert tok == expected_tokens[i], f"Expected {expected_tokens[i]}, but got {tok}"


def test_skip_whitespace():

    lexer = Lexer("a = 12")

    expected_tokens = [
        Token(token.IDENT, "a"),
        Token(token.ASSIGN, "="),
        Token(token.INT, "12")
    ]

    for i in range(len(expected_tokens)):
        lexer.readChar()
        tok = lexer.nextToken()
        assert tok == expected_tokens[i], f"Expected {expected_tokens[i]}, but got {tok}"


def test_all():
    lexer = Lexer('''
let five = 5;
let ten = 10;

let add = fn(x, y) {
  x + y;
};

let result = add(five, ten);
!-/*5;
5 < 10 > 5;

if (5 < 10) {
	return true;
} else {
	return false;
}

10 == 10;
10 != 9;
    ''')

    expected_tokens = [
		Token(token.LET, "let"),
		Token(token.IDENT, "five"),
		Token(token.ASSIGN, "="),
		Token(token.INT, "5"),
		Token(token.SEMICOLON, ";"),
		Token(token.LET, "let"),
		Token(token.IDENT, "ten"),
		Token(token.ASSIGN, "="),
		Token(token.INT, "10"),
		Token(token.SEMICOLON, ";"),
		Token(token.LET, "let"),
		Token(token.IDENT, "add"),
		Token(token.ASSIGN, "="),
		Token(token.FUNCTION, "fn"),
		Token(token.LPAREN, "("),
		Token(token.IDENT, "x"),
		Token(token.COMMA, ","),
		Token(token.IDENT, "y"),
		Token(token.RPAREN, ")"),
		Token(token.LBRACE, "{"),
		Token(token.IDENT, "x"),
		Token(token.PLUS, "+"),
		Token(token.IDENT, "y"),
		Token(token.SEMICOLON, ";"),
		Token(token.RBRACE, ")"),
		Token(token.SEMICOLON, ";"),
		Token(token.LET, "let"),
		Token(token.IDENT, "result"),
		Token(token.ASSIGN, "="),
		Token(token.IDENT, "add"),
		Token(token.LPAREN, "("),
		Token(token.IDENT, "five"),
		Token(token.COMMA, ","),
		Token(token.IDENT, "ten"),
		Token(token.RPAREN, ")"),
		Token(token.SEMICOLON, ";"),
		Token(token.BANG, "!"),
		Token(token.MINUS, "-"),
		Token(token.SLASH, "/"),
		Token(token.ASTERISK, "*"),
		Token(token.INT, "5"),
		Token(token.SEMICOLON, ";"),
		Token(token.INT, "5"),
		Token(token.LT, "<"),
		Token(token.INT, "10"),
		Token(token.GT, ">"),
		Token(token.INT, "5"),
		Token(token.SEMICOLON, ";"),
		Token(token.IF, "if"),
		Token(token.LPAREN, "("),
		Token(token.INT, "5"),
		Token(token.LT, "<"),
		Token(token.INT, "10"),
		Token(token.RPAREN, ")"),
		Token(token.LBRACE, "{"),
		Token(token.RETURN, "return"),
		Token(token.TRUE, "true"),
		Token(token.SEMICOLON, ";"),
		Token(token.RBRACE, ")"),
		Token(token.ELSE, "else"),
		Token(token.LBRACE, "{"),
		Token(token.RETURN, "return"),
		Token(token.FALSE, "false"),
		Token(token.SEMICOLON, ";"),
		Token(token.RBRACE, ")"),
		Token(token.INT, "10"),
		Token(token.EQ, "=="),
		Token(token.INT, "10"),
		Token(token.SEMICOLON, ";"),
		Token(token.INT, "10"),
		Token(token.NOT_EQ, "!="),
		Token(token.INT, "9"),
		Token(token.SEMICOLON, ";"),
		Token(token.EOF, ""),
    ]
if __name__ == "__main__":
    ...
