notas = [] 
for _ in range(4):
    notas.append(float(input('Digite a nota: ')))
media = sum(notas) / len(notas)
if media >= 7.0:
    print(f'O aluno foi aprovado com média {media:.2f}')
else:
    print(f'O aluno foi reprovado com média {media:.2f}')
