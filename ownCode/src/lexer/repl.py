
from lexer import Lexer

prompt: str = '>>'

def start():
    while True:
        code: str = input(prompt)

        lexer = Lexer(code)

        while lexer.read_position <= len(lexer.input):
            lexer.readChar()
            tok = lexer.nextToken()
            print(tok)


if __name__ == '__main__':
    start()
