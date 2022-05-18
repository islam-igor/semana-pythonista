'''

# questão 1 - somar os numeros multiplos de 3 entre 0 e 500!
lista = list(range(0,500,3))

total = 0 

for soma in lista:
    total += soma

print(total)

'''

'''

# questão 2 - ler 7 anos e dizer quantas sao maiores e menores de idade

maior = 0
contador = 0
menor = 0


while contador < 7:
    ano = int(input("Digite o ano que você nasceu \n"))
    if 2022 - ano < 18:
        menor = menor + 1
    else:
        maior = maior + 1
    contador = contador + 1
    
print(f'temos {maior} pessoas maior de idade')
print(f'temos {menor} pessoas menor de idade')

'''

'''

# questão 3 - população

def pop(A, B, tx_a, tx_b, ano = 0):
    while A < B:
        ano = ano + 1
        A = A*(1+tx_a)
        B = B*(1+tx_b)
    
    print(f"a cidade A ultrapassa ou igual a população de B em {ano} anos")
    print(f' a população de A será = {A:.0f} e de B = {B:.0f}')

pop(80000, 200000, 3/100, 1.5/100)

'''

# questão 4 - população





def qt_digito():
    x = str(input("Digite um numero inteiro"))
    print(len(x))

qt_digito()
