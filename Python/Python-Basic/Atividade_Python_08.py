
# input() recebe dados digitados, mas o resultado vem como texto.
# float() transforma o texto em um numero que pode ter casas decimais.
# Para calcular a media: (nota1 + nota2) / 2
# Exemplo de conversao: nota1 = float(input("Digite a primeira nota: "))
# Exemplo da formula: media = (nota1 + nota2) / 2

(n1) = float(input('Digite o primeiro número:'))
(n2) = float(input('Digite o segundo número:'))

if n1 > n2:
    print('O maior número é:' , n1)
elif n2 > n1:
    print('O maior número é:' , n2)
