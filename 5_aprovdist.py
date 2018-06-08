#aprovdist.py

n1 = int(
	input(
	'Digite sua primeira nota parcial: '
))
n2 = int(
	input(
		'Digite a segunda nota parcial: '
))

nf = (n1 + n2) / 2

if nf >= 7 and nf < 10:
	print(
		'\nAPROVADO!\n'
)
elif nf == 10:
	print(
		'\nAPROVADO COM DISTINÇÃO!\n'
)
else:
	print(
		'\nREPROVADO!\n'
)