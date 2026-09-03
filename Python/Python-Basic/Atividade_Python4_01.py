
#Login de caixa
#-----------------------------------------------------------------------------------------------------------------------------------------
user = input('Insira o nome de ususário:')
pin = input('Insira a senha:')
while user == pin:
    print('Acesso negado, nome de usuário e senha não podem ser iguais.')
    pin = input('Insira a senha novamente: ')
print('acesso permitido')
#Cálculo do desconto
#-------------------------------------------------------------------------
def cart(*produto):
    total = 0
    precos = []
    for item in produto:
        total += item[1] * item[2]
        precos.append(item[2])
    maior = max(produto, key=lambda item: item[2])
    menor = min(produto, key=lambda item: item[2])
    media = sum(precos) / len(precos)
    if total > 100:
        total *= 0.9
    return total, maior, menor, media
#Criação do carrinho
#-------------------------------------------------------------------------
produto = []
while True:
    novo_produto = input('Adicione um produto: ')
    if novo_produto == 'sair':
        break
    quantidade = int(input('Quantidade: '))
    preco = float(input('Insira o valor unitário: R$ '))
    produto.append([novo_produto, quantidade, preco])
total_final, maior, menor, media = cart(produto)
print(f'Total da compra: R$ {total_final:.2f}')
print(f'O produto mais caro é: {maior:.2f} e o mais barato é: {menor:.2f}')
print(f'A média dos produtos é: {media:.2f}')
#Produtos em promoção
#-------------------------------------------------------------------------
promocao = ('Café', 'Pão Francês', 'Leite', 'Açúcar', 'Manteiga')
prod_consul = input('Insira o produto: ')
if prod_consul in promocao:
    print('Produto em promoção!')
else:
    print('Produto fora da promoção.')

