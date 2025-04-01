from dataclasses import dataclass

type TokenType = str

ILLEGAL = "ILLEGAL"
EOF     = "EOF"

# Identifiers + literals
IDENT = "IDENT" # add, foobar, x, y, ...
INT   = "INT"   # 1343456

# Operators
ASSIGN   = "="
PLUS     = "+"
MINUS    = "-"
BANG     = "!"
ASTERISK = "*"
SLASH    = "/"

LT = "<"
GT = ">"

EQ     = "=="
NOT_EQ = "!="

# Delimiters
COMMA     = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"

# Keywords
FUNCTION = "FUNCTION"
LET      = "LET"
TRUE     = "TRUE"
FALSE    = "FALSE"
IF       = "IF"
ELSE     = "ELSE"
RETURN   = "RETURN"

keywords: dict[str, TokenType] = {
    "fn": FUNCTION,
    "let": LET,
    "true": TRUE,
    "false": FALSE,
    "if": IF,
    "else": ELSE,
    "return": RETURN
}


@dataclass
class Token:
    type: TokenType
    literal: str

    def __repr__(self):
        return f"Token(type={self.type}, literal={self.literal})"

    def lookupIdent(self) -> TokenType:
        """Check if literal is a keyword"""
        if self.literal in keywords:
            return keywords[self.literal]
        else:
            return IDENT

