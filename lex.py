import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """

    token_specification = [
        ('LPAR', r'\('),
        ('RPAR', r'\)'),
        ('BOOL', r'#[t|f]'),
        ('NUMBER',   r'(\+|\-)?\d+(\.\d*)?([eE][+-]?\d+)?'),
        ('STRING', r'\"(.+\'?)\"'),
        ('NAME', r'([^()\"\n \#\;]+)'),
        ('CHAR', r'\#\\(\w|\d)+'),
        ('COMMENT', r'\;([\w\ \d \S])+'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'COMMENT':
            continue
        
        yield Token(kind, value)
