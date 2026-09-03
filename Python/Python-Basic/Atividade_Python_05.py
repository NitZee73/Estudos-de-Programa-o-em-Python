
# input() recebe dados digitados, mas o resultado vem como texto.
# float() transforma o texto em um numero que pode ter casas decimais.
# Para calcular a media: (nota1 + nota2) / 2
# Exemplo de conversao: nota1 = float(input("Digite a primeira nota: "))
# Exemplo da formula: media = (nota1 + nota2) / 2

mtr = input ("Digite a os metros a serem convertidos: ")
cm = float(mtr)*100
print ("A converção em centimetros é: ", cm)
