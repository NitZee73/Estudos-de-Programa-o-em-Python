
# input() recebe dados digitados, mas o resultado vem como texto.
# float() transforma o texto em um numero que pode ter casas decimais.
# Para calcular a media: (nota1 + nota2) / 2
# Exemplo de conversao: nota1 = float(input("Digite a primeira nota: "))
# Exemplo da formula: media = (nota1 + nota2) / 2

n = int(input('Digite um número entre 0 e 10: '))
while n < 0 or n > 10:
    print('Número inválido! Digite um número entre 0 e 10.')
    n = int(input('Digite um número entre 0 e 10: '))

