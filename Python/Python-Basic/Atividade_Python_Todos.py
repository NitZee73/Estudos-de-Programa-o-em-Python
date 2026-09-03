# ==================================================
# EXERCICIO 01 - Ola Mundo
# ==================================================
print('Olá Mundo!')


# ==================================================
# EXERCICIO 02 - Numero informado
# ==================================================
numero = input("Digite um número: ")
print('O número digitado é: ', numero)


# ==================================================
# EXERCICIO 03 - Numero informado em uma mensagem
# ==================================================
numero = input("Digite um numero: ")
print("O numero informado foi", numero)


# ==================================================
# EXERCICIO 04 - Media de quatro notas
# ==================================================
nota1 = input("Digite a primeiro nota: ")
nota2 = input("Digite a segunda nota: ")
nota3 = input("Digite a terceira nota: ")
nota4 = input("Digite a quarta nota: ")

media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4
print('A media das notas é: ', media)


# ==================================================
# EXERCICIO 05 - Conversao de metros para centimetros
# ==================================================
mtr = input("Digite os metros a serem convertidos: ")
cm = float(mtr) * 100
print("A conversao em centimetros e: ", cm)


# ==================================================
# EXERCICIO 06 - Area do circulo
# ==================================================
raio = input("Digite o valor do raio: ")
a = 3.14 * (float(raio) ** 2)
print("A area do circulo e:", a)


# ==================================================
# EXERCICIO 07 - Dobro da area do quadrado
# ==================================================
lado = input("Digite o valor do lado do quadrado: ")
area = (float(lado) * float(lado)) * 2
print('O dobro da area do quadrado e: ', area)


# ==================================================
# EXERCICIO 08 - Maior entre dois numeros
# ==================================================
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

if n1 > n2:
    print('O maior numero e:', n1)
elif n2 > n1:
    print('O maior numero e:', n2)


# ==================================================
# EXERCICIO 09 - Numero positivo ou negativo
# ==================================================
n = float(input('Digite um numero: '))

if n > 0:
    print('O numero e positivo')
elif n < 0:
    print('O numero e negativo')


# ==================================================
# EXERCICIO 10 - Situacao do aluno
# ==================================================
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2
if media == 10:
    print('Aprovado com Distincao')
elif media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')


# ==================================================
# EXERCICIO 11 - Numero entre 0 e 10
# ==================================================
n = int(input('Digite um numero entre 0 e 10: '))
while n < 0 or n > 10:
    print('Numero invalido! Digite um numero entre 0 e 10.')
    n = int(input('Digite um numero entre 0 e 10: '))


# ==================================================
# EXERCICIO 12 - Nome de usuario e senha
# ==================================================
nome = input('Digite o nome de usuario: ')
senha = input('Digite a senha: ')

while senha == nome:
    print('A senha nao pode ser igual ao nome de usuario. Digite novamente.')
    senha = input('Digite a senha: ')
