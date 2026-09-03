# ==================================================
# ATIVIDADE PYTHON 3 - EXERCICIO 01
# ==================================================


def apresentar_curso(nome, curso):
    print(f'Olá {nome}, seja benvido ao curso de {curso}!')


nome = input('Digite seu nome: ')
curso = input('Digite o curso que você iniciará: ')

apresentar_curso(nome, curso)


# ==================================================
# ATIVIDADE PYTHON 3 - EXERCICIO 02
# ==================================================


def metros_para_centimetros(metros):
    centimetros = metros * 100
    print(f'O valor em centímetros é: {centimetros} cm')


metros = float(input('Digite o valor em metros: '))
metros_para_centimetros(metros)


# ==================================================
# ATIVIDADE PYTHON 3 - EXERCICIO 03
# ==================================================


def media_final(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    print(f'A média final do aluno é: {media:.2f}')
    return media


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = media_final(n1, n2, n3)

if media >= 7:
    print('O aluno foi aprovado!')
else:
    print('O aluno foi reprovado!')


# ==================================================
# ATIVIDADE PYTHON 3 - EXERCICIO 04
# ==================================================


def verif_peca(peca):
    if peca < 50:
        print('A peça deve ter no mínimo 50g. Reprovada!')
    elif peca > 100:
        print('A peça possui peso acima de 100g. Reprovada!')
    else:
        print('A peça está dentro do peso ideal. Aprovada!')


peso_peca = float(input('Digite o peso da peça em gramas: '))
verif_peca(peso_peca)


# ==================================================
# ATIVIDADE PYTHON 3 - EXERCICIO 05
# ==================================================


def calc_inss(salario_bruto):
    if salario_bruto <= 2000.00:
        inss = salario_bruto * 0.07
    else:
        inss = salario_bruto * 0.09
    salario_final = salario_bruto - inss
    return salario_final


salario_bruto = float(input('Digite o salário bruto do funcionário: R$ '))
salario_final = calc_inss(salario_bruto)
print(f'O salário final do funcionário é: R$ {salario_final:.2f}')
