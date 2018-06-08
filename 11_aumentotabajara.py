#aumentotabajara.py

salario_antes = float(
	input(
		'Digite seu salário atual: '
))

if salario_antes <= 280:
	aumento = (salario_antes * 20) / 100
	salario_final = salario_antes + aumento

	print(
		'\n',
		'Salário antes do reajuste: ------------- R$ %.2f' %salario_antes,
		'\n',
    	'Você terá uma porcentagem de aumento de: 20%',
    	'\n',
    	'você terá um aumento de: --------------- R$ %.2f' %aumento,
      	'\n',
    	'O seu salário após o aumento será de: -- R$ %.2f' %salario_final,
    	'\n'
)
elif salario_antes <= 700:
	aumento = (salario_antes * 15) / 100
	salario_final = salario_antes + aumento

	print(
		'\n',
		'Salário antes do reajuste: ------------- R$ %.2f' %salario_antes,
		'\n',
    	'Você terá uma porcentagem de aumento de: 15%',
    	'\n',
    	'você terá um aumento de: --------------- R$ %.2f' %aumento,
      	'\n',
    	'O seu salário após o aumento será de: -- R$ %.2f' %salario_final,
    	'\n'
)
elif salario_antes <= 1500:
	aumento = (salario_antes * 10) / 100
	salario_final = salario_antes + aumento

	print(
		'\n',
		'Salário antes do reajuste: ------------- R$ %.2f' %salario_antes,
		'\n',
    	'Você terá uma porcentagem de aumento de: 10%',
    	'\n',
    	'você terá um aumento de: --------------- R$ %.2f' %aumento,
      	'\n',
    	'O seu salário após o aumento será de: -- R$ %.2f' %salario_final,
    	'\n'
)
else:
	aumento = (salario_antes * 5) / 100
	salario_final = salario_antes + aumento

	print(
		'\n',
		'Salário antes do reajuste: ------------- R$ %.2f' %salario_antes,
		'\n',
    	'Você terá uma porcentagem de aumento de: 5%',
    	'\n',
    	'você terá um aumento de: --------------- R$ %.2f' %aumento,
      	'\n',
    	'O seu salário após o aumento será de: -- R$ %.2f' %salario_final,
    	'\n'
)