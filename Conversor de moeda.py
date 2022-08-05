real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.23
euro = real / 5.34
print('Com R$ {:.2f} você pode comprar U$ {:.2f}'.format(real, dolar))
print('Com R$ {:.2f} você pode comprar EUR {:.2f}'.format(real, euro))
