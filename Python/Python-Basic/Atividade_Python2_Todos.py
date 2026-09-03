# Atividade_Python2_01.py
amigos = ["João", "Maria", "Pedro",]
amigos.append("Ana")
print(amigos[2])


# Atividade_Python2_02.py
computador = ['Processador', 'Memória RAM', 'HD']
computador [2] = 'SSD'
print(computador)


# Atividade_Python2_03.py
lista = [1,2,3,4,2,5,5,5]
busca = int(input("Digite um número: "))
qtd = lista.count(busca)
print(f'O número {busca} aparece {qtd} vezes')


# Atividade_Python2_04.py
alunos = [input('Digite os nomes dos alunos: ')]

for _ in range(3):
	alunos.append(input('Digite os nomes dos alunos: '))

print(alunos)


# Atividade_Python2_05.py
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
for numero in numeros:
    if numero % 2 ==0:
        print(f'Os números pares são: {numero}')


# Atividade_Python2_06.py
notas = [] 
for _ in range(4):
    notas.append(float(input('Digite a nota: ')))
media = sum(notas) / len(notas)
if media >= 7.0:
    print(f'O aluno foi aprovado com média {media:.2f}')
else:
    print(f'O aluno foi reprovado com média {media:.2f}')


# Atividade_Python2_07.py
precos = [250.00, 180.00, 420.00, 310.00, 150.00]
print(f'Maior preço: R$ {max(precos):.2f}')
print(f'Menor preço: R$ {min(precos):.2f}')


# Atividade_Python2_08.py
pecas = [f'Memoria , PlacaMae , PlacaVideo , Processafor , Fonte , Cooler , SSD , HD']

busca = input('Digite o nome da peça que deseja verificar: ')
if busca in pecas:
    print(f'A peça {busca} está disponível.')
else:
    print(f'A peça com o nome {busca} não foi encontrada ou o nome está incorreto. Por favor tente novamente')


# Atividade_Python2_09.py
sistemas = ["Windows", "Android", "Linux", "iOS", "macOS"]
mobile = []
desktop = []

for so in sistemas:
    if so == "Android" or so == "iOS":
        mobile.append(so)
    else:
        desktop.append(so)

print("Sistemas operacionais móveis:", mobile)
print("Sistemas operacionais de desktop:", desktop)


# Atividade_Python2_10.py
carrinho = []
while True:
    produto = input('Digite o nome do produto (ou "sair" para encerrar): ')
    if produto.lower () == 'sair':
        break
    carrinho.append(produto)
    print(f'iten adicionado no carrinho: {carrinho}')
