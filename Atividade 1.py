#ano = int(input('Qual ano você nasceu?'))
#print(f'Então em 2035 você fará {2035-ano}')

'''
numero = float(input('Digite um número:'))

ant = int(numero)

if ant == numero:
    print(f'o antecessor inteiro de {numero} é {ant-1}')
else:
    print(f'o antecessor inteiro de {numero} é {ant}')

suc = int(numero) +1

print(f'o sucessor inteiro de {numero} é {suc}')
'''

larg = float(input('Qual a Largura da Parede em metros?'))
alt = float(input('Qual a Altura da Parede em metros?'))

area = larg*alt
print(f'a area da parede é de {area} metros quadrados')

tinta = area/2

print(f'para pintar 1 lado da parede gastaremos {tinta} Litros de tinta, para pintar as duas faces {2*tinta} Litros.')