print('-' * 40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-' * 40)
totpreço = totmil = menor = cont = 0
barato = ''
while True: 
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    cont += 1
    conti = ' '
    totpreço += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    while conti not in 'SN':
        conti = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if conti == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${totpreço:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')