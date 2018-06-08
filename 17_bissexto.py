#bissexto.py

"""

17. Faça um Programa que peça um número correspondente a um determinado ano 
e em seguida informe se este ano é ou não bissexto. 

"""

ano = int(
	input(
		'Digite o ano: '
))

if ano % 4 == 0 and ano % 100 != 0:
	print(
		'\nO ano é bissexto!\n'
)
else:
	print(
		'\nO ano não é bissexto!\n'
)