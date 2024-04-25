VALOR = 26
C = 1
resposta = int(input('Informe o valor correto: '))
if resposta != VALOR:
    print()
    print('Dica: o número é menor que 30 e maior que 20')
    print()
while resposta != VALOR:
    resposta2 = int(input('Informe o valor correto: '))
    resposta = resposta2
    C += 1
print('Tentativas:', C)
