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
        ('NUMBER',   r'(\+|\-)?\d+(\.\d*)?([eE][+-]?\d+)?'),  # Integer or decimal number
        ('STRING', r'\"(.+\'?)\"'),
        ('NAME', r'([^()\"\n \#\;]+)'),
        ('CHAR', r'\#\\(\w|\d)+'),
        ('COMENT', r'\;\;([\w\ \d \S])+'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'COMENT':
            continue
        yield Token(kind, value)

# exemplos = [
#     """(#t #f)""",
#     """(#f)""",
#     """("uma string bad as")""",
#     """("hello-world")""",
#     """("hello_world")""",
#     """("hello$world")""",
#     """("hello&world")""",
#     """("hello_world")""",
#     """("hello_world")""",
#     """("!@#$%&*")""",
#     """('1 2.0 -1 3.14 42.0 +100')""",
#     """( 'max x y' )""",

# ]
# for ex in exemplos:
#     print(ex)
#     for tok in lex(ex):
#         print('    ', tok)
#     print()