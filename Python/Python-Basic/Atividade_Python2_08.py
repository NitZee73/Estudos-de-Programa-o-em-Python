pecas = [f'Memoria , PlacaMae , PlacaVideo , Processafor , Fonte , Cooler , SSD , HD']

busca = input('Digite o nome da peça que deseja verificar: ')
if busca in pecas:
    print(f'A peça {busca} está disponível.')
else:
    print(f'A peça com o nome {busca} não foi encontrada ou o nome está incorreto. Por favor tente novamente')
