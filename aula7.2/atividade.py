# def multi(x):
#     D = x * 2
#     T = x * 3
#     Q = x ** 2
#     print(f'{D}, {T},{Q}')


# num = int(input('Qual o numero: '))

# calculo = multi(num)

peixe = int(input('Quantos kg de peixe voce pegou?: '))

LIMITE = 100
B = peixe - LIMITE

if B <= 0:
    print('Ta tudo certo')

else:
    def soma(x):
        p = x * 4
        return p
C = soma(B)
print(f'vc tera que pagar R${C} de multa')
