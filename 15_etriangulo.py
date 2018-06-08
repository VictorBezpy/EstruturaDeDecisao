#etriangulo.py

l1 = float(
	input(
		'Valor primeiro lado: '
))
l2 = float(
	input(
		'Valor segundo lado: '
))
l3 = float(
	input(
		'Valor terceiro lado: '
))

if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
	print(
		'\nNão é um triângulo.\n'
)  
else:
	print(
		'\nÉ um triângulo.\n'
)
	if l1 == l2 and l1 == l3:
		print(
			'\nÉ equilátero.\n'
)
	elif l1 == l2 or l1 == l3 or l2 == l3:
		print(
			'\nÉ isósceles.\n'
)
	else:
		print(
			'\nÉ escaleno.\n'
)