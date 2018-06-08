#brutoate.py

"""

12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela
abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde 
ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor 
da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações.


"""
#ganho por hora.
gph = input(
    'Digite quando você ganha por hora: '
)
#horas trabalhadas no mês.
htm = input(
    'Digite o número de horas trabalhadas no mês: '
)
#Salário bruto = ganho por hora * horas trabalhadas no mês.
sb = float(gph) * float(htm)

#Imposto de renda.
if sb <= 900:
    ir = 0
elif sb <= 1500:
    ir = (float(sb) * 5) /100
elif sb <= 2500:
    ir = (float(sb) * 10) /100
else:
    ir = (float(sb) * 20) /100

#FGTS = 11% do salário bruto.
inss = (float(sb) * 11) / 100

# 3% do salário bruto = contribuição sindical
sind = (float(sb) * 3) / 100

#Salário Líquido = salário bruto - (imposto de renda + INSS + sindicato)
sl = sb - (float(ir) + float(inss) + float(sind))


#'\n' para dar uma linha para a tabela, espaços nas strings para alinhar
#round(xxx, 2) para restringir a casa à direita até duas.
print(
    '\n',
    '+ Salário Bruto :   R$  ',
    round(sb, 2),
    '\n',
    '- IR  :             R$  ',
    round(ir, 2),
    '\n',
    '- FGTS (11%) :      R$  ',
    round(inss, 2),
    '\n',
    '- Sindicato (3%) :  R$  ',
    round(sind, 2),
    '\n',
    '= Salário Liquido : R$ ',
    round(sl, 2),
    '\n'
)