from distutils.log import error
from mailbox import NotEmptyError


def soma(x,y):                              # as variáveis dentro de uma função, só existem dentro dela
    resultado = x + y                       # para utilizar valores de uma função
                                            # é necessário utilizar o 'return'
    return resultado

resultado = soma(3,54)
print(resultado)


#Para que o programe nao trave e apresente um erro, utiliza-se o TRY (tente)

a = 1 
b = 'a'

try:                                                #tente fazer algo, se nao consegue faça EXCEPT
    a/b
except ZeroDivisionError:                           #exceção de um erro específico
    print("o valor de b é igual a zero e nao pode ser dividido")
except TypeError:
    print("não podemos dividir um numero por uma string")
except:                                             #qualquer outro erro
    print(error)


class MinhaClasse:  # É costumeiro usar a formatação 'Camelo' para identificar classes 'FormataçãoTipoCamelo'
    numero = 12345
    
    def metodo(self):     # por padrão, sempre que tem uma def dentro de uma classe deverá ter o (self)
        return 'Olá Mundo'
        

    def soma(self, x,y):                              # as variáveis dentro de uma função, só existem dentro dela
        resultado = x + y                       # para utilizar valores de uma função
                                            # é necessário utilizar o 'return'
        return resultado

print(MinhaClasse().soma(3,5))

class Cachorro:
    def ir_dormir(self):                     #Caracteristicas que todos os cachorros tem
        return f'O {self.nome} foi dormir'
    def comer(self):                         #Caracteristicas que todos os cachorros tem
        return f'O {self.nome} foi comer'
    def correr(self):                        #Caracteristicas que todos os cachorros tem
        return f'O {self.nome} foi correr'
    def acordou(self):                       #Caracteristicas que todos os cachorros tem
        return f'O {self.nome} foi acordar'
    
    def __init__ (self,nome='Cachorro',idade='não definida'):                    ###CARACTERISTICA INDIVIDUAL PARA CADA CACHORRO###
        self.nome = nome
        self.idade = idade
        
#(Cachorro().comer())
pingo = Cachorro(nome='Pingo', idade='2 anos')

print(pingo.comer())
print(Cachorro().comer())

mel = Cachorro(nome='Mel', idade='1 ano')

print(mel.ir_dormir())