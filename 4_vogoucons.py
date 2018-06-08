#vogoucons.py

l = str(
    input(
        'digite uma letra: '
))

if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
    print(
        '\na letra',
        str(l),
        'é uma vogal!\n'
)
else:
    print(
        '\na letra',
        str(l),
        'é uma consoante!\n'
)