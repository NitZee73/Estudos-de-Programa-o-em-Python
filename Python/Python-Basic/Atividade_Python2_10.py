carrinho = []
while True:
    produto = input('Digite o nome do produto (ou "sair" para encerrar): ')
    if produto.lower () == 'sair':
        break
    carrinho.append(produto)
    print(f'iten adicionado no carrinho: {carrinho}')
