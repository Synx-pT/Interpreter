
from dataclasses import dataclass
from typing import Union

@dataclass
class Lexer:
    input: str
    position: int = 0
    read_position: int = 0
    ch: Union[str, None] = '' # Current character

    def readChar(self) -> None:
        if self.read_position > len(self.input):
            self.ch = None
        else:
            self.ch = self.input[self.read_position]

        self.position = self.read_position
        self. read_position += 1

    def nextChar(self) -> None:
        ...
