def verif_peca(peca):
    if peca < 50:
        print('A peça deve ter no mínimo 50g. Reprovada!')
    elif peca > 100:
        print('A peça possui peso acima de 100g. Reprovada!')
    else:
        print('A peça está dentro do peso ideal. Aprovada!')

peso_peca = float(input('Digite o peso da peça em gramas: '))
verif_peca(peso_peca)