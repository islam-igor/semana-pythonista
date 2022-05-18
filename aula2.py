'''
            PARTE 1 (IF, ELIF, ELSE)
altura = float(input("Qual sua altura em metros")) 
peso =  float(input("Qual o seu peso em KG"))

imc = peso / (altura**2)
print(f'seu imc é {imc}')

if imc < 18.5 :
    print('você se encontra abaixo do peso')
elif imc < 25:
    print("peso normal")
elif imc < 30:
    print("sobrepeso")
elif imc < 35:
    print("obseidade grau l")
elif imc < 40:
    print("obseidade grau l")
else:
    print("obesidade grau 3 ou morbida")

'''


'''      
# PARTE 2 (WHILE)
a = 0

while a < 5:                       #enquanto uma condição for TRUE ele repete até ser FALSE
    print(f'O valor de a={a}')
    a = a + 1

print(a)

'''

'''
# PARTE 3 (FOR) laçõ de repetição usado em LISTAS
lista = [2 ,3, 'abc', 10.189]
print(type(lista))

for elem in lista:    #para cada item da lista ele vai executar essa sequencia de código
    print(elem)
print('\n')
                # MELHORANDO A CALCULADORA DE MÉDIA

materias = ['português','matemática','história','inglês','geografia']

soma = 0 

for materia in materias:
    nota = float(input(f"Qual a nota do aluno em {materia} "))
    soma = soma + nota

media = soma / (len(materias))

print(f'a media do aluno é de {media}')

'''


# PARTE 4 (def) 

def boas_vindas(nome='', curso=''):
    print(f'{nome} Bem vindo ao curso de {curso}')

boas_vindas(nome= input('seu nome'), curso= input('seu curo'))


