#turno.py

s = str(
    input(
        'digite seu turno de trabalho, "m" para matutino, "v" para vespertino e "n" para noturno : '
))

if s == 'm':
    print(
        '\nBom dia!\n'
)
elif s == 'v':
    print(
        '\nBoa tarde!\n'
)
elif s == 'n':
    print(
        '\nBoa noite!\n'
)
else:
    print(
        '\nValor inválido!\n'
)