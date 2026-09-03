
# input() recebe dados digitados, mas o resultado vem como texto.
# float() transforma o texto em um numero que pode ter casas decimais.
# Para calcular a media: (nota1 + nota2) / 2
# Exemplo de conversao: nota1 = float(input("Digite a primeira nota: "))
# Exemplo da formula: media = (nota1 + nota2) / 2

lado = input("Digite o valor do lado do quadrado: ")

area = (float(lado) * float(lado)) * 2
print(' O dobro da área do quadrado é: ',area)