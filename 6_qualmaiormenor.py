#qualmaiormenor.py

a = int(
    input(
        'primeiro: '
))

b = int(
    input(
        'segundo: '
))

c = int( 
    input(
        'terceiro: '
))

if a >= b and a >= c:
    print(
        '\no primeiro é maior!\n'
)
elif b >= a and b >= c:
    print(
        '\no segundo é maior!\n'
)
else:
    print(
        '\no terceiro é maior!\n'
)

if a <= b and a <= c:
    print(
        '\ne o primeiro é menor!\n'
)
elif b <= a and b <= c:
    print(
        '\ne o segundo é menor!\n'
)
else:
    print(
        '\ne o terceiro é menor!\n'
)