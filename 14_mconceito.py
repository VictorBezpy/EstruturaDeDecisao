#mconceito

n1 = float(
	input(
		'Primeira nota: '
))
n2 = float(
	input(
		'Segunda nota: '
))
n3 = float(
	input(
		'Terceira nota: '
))

nf = (n1 + n2 + n3) / 3

if nf >= 9:
	print(
		'\nNotas: %.2f, %.2f, %.2f' %(n1, n2, n3),
		'\n',
		'Média: %.2f' %nf,
		'\n',
		'Conceito: A',
		'\n',
		'Aprovado!',
		'\n'
)
elif nf >= 7.5:
	print(
		'\nNotas: %.2f, %.2f, %.2f' %(n1, n2, n3),
		'\n',
		'Média: %.2f' %nf,
		'\n',
		'Conceito: B',
		'\n',
		'Aprovado!',
		'\n'
)
elif nf >= 6:
	print(
		'\nNotas: %.2f, %.2f, %.2f' %(n1, n2, n3),
		'\n',
		'Média: %.2f' %nf,
		'\n',
		'Conceito: C',
		'\n',
		'Aprovado!',
		'\n'
)
elif nf >= 4:
	print(
		'\nNotas: %.2f, %.2f, %.2f' %(n1, n2, n3),
		'\n',
		'Média: %.2f' %nf,
		'\n',
		'Conceito: D',
		'\n',
		'Reprovado!',
		'\n'
)
else:
	print(
		'\nNotas: %.2f, %.2f, %.2f' %(n1, n2, n3),
		'\n',
		'Média: %.2f' %nf,
		'\n',
		'Conceito: E',
		'\n',
		'Reprovado!',
		'\n'
)

