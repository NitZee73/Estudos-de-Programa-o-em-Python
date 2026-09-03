
# input() recebe dados digitados, mas o resultado vem como texto.
# float() transforma o texto em um numero que pode ter casas decimais.
# Para calcular a media: (nota1 + nota2) / 2
# Exemplo de conversao: nota1 = float(input("Digite a primeira nota: "))
# Exemplo da formula: media = (nota1 + nota2) / 2

nota1 =input("Digite a primeiro nota: ")
nota2 =input("Digite a segunda nota: ")
nota3 =input("Digite a terceira nota: ")
nota4 =input("Digite a squarta nota: ")

media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4

print('A media das notas é: ', media)