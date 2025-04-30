# funçoes em python inicia com a palavra
# reservada def.
# Funções são rotinas em seu conceito
# são blocos que são executados se forem chamados

# def saudacao():
#     print('Olá mundo')


# saudacao()

# def mostrar_linha():
#     print(38*"=")


# mostrar_linha()
# print('MODULO 1')
# mostrar_linha()
# print('ANALISE')
# mostrar_linha()
# print('ALGORITIOMOS')

# def saudacao(nome):
#     print(f'Olá, {nome}')


# nome = input('qual o seu nome: ')
# saudacao(nome)

def somar(a, b):
    soma = a + b
    print(soma)


soma = 0
somar(4, 5)
print(f'O valor da variavel soma é {soma}')

def somar_numeros(x, y):
    s = x + y
    return s


# for i in range(3):
#     n1 = int(input('Informe o numero: '))
#     n2 = int(input('Informe o numero: '))

#     soma = somar_numeros(n1, n2)
#     print(soma)
