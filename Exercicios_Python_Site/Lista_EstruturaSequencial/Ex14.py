"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
"""
peso_do_peixe = float(input("Informe o peso do peixe: "))

if peso_do_peixe > 50:
    
    excesso = peso_do_peixe - 50
    multa = excesso * 4.0
    print("O excesso do peso é {0} kilo".format(excesso))
    print("O valor da multa a ser paga é: R${0}".format(multa))
else:
    print("O peso do seu peixe esta dentro do estabelecido.")