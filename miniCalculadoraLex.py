import ply.lex as lex
import sys

# Lista de tokens
reserved = {
    'sin': 'FUNCIONSIN',
    'cos': 'FUNCIONCOS',
    'log': 'FUNCIONLOG'
}
tokens = (
    'NUMERO',
    'ID',
    'MAS',
    'MENOS',
    'PARENTESIS_I',
    'PARENTESIS_D',
    'MULTIPLICACION',
    'DIVISION',
    'PUNTO',
    'EXPONENTE',
    'FACTORIAL',
    'FUNCIONSIN',
    'FUNCIONCOS',
    'FUNCIONLOG'
)

# Expresiones regulares para los tokens de símbolos
t_MAS             = r'\+'
t_MENOS           = r'-'
t_MULTIPLICACION  = r'\*'
t_DIVISION        = r'/'
t_PARENTESIS_I    = r'\('
t_PARENTESIS_D    = r'\)'
t_PUNTO           = r'\.'
t_EXPONENTE       = r'(\*\*|\^)'
t_FACTORIAL       = r'!'

# Regla para reconocer números: enteros o flotantes (con parte decimal opcional)
def t_NUMERO(t):
    r'(-)?\d+(\.\d+)?([eE][-+]?\d+(\.\d+)?)?'
    return t

# Regla para identificar identificadores (por ejemplo, nombres de funciones matemáticas)
def t_ID(t):
    r'\w+(_\d\w)*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

# Regla para reconocer saltos de línea y actualizar el contador de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres a ignorar (espacios y tabulaciones)
t_ignore  = ' \t'

# Manejo de errores léxicos
def t_error(t):
    print("Lexical error: " + str(t.value[0]) + " en la línea " + str(t.lineno))
    t.lexer.skip(1)

# Función para probar el analizador con una cadena de entrada
def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Construcción del lexer
lexer = lex.lex()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = sys.argv[1]
    else:
        fin = 'evaluacion.py'
    with open(fin, 'r') as f:
        data = f.read()
    print("Contenido del archivo:")
    print(data)
    print("\nTokens encontrados:")
    test(data, lexer)
