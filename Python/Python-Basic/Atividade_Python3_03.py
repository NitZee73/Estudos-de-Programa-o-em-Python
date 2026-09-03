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