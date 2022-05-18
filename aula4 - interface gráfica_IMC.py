import tkinter as tk
from tkinter import Button, Entry, Frame, Label #alternativa para nao ter que chamar a função tk.Label()

def calcula_imc():
    imc = float(peso.get()) / float(altura.get()) **2
    resultado['text'] = f'O seu IMC é {imc}'
    print(f'O seu IMC é {imc}')

janela = tk.Tk()

frame = Frame(janela, padx=40, pady=40).grid(column=1, row=1) #cria uma janela invisivel para encapsular outros elementos
            #semelhante ao section do HTML
#Label(janela, text='Para saber seu IMC digite os valores abaixo', pady=40, padx=40).grid(column=1, row=1)  #pack (mais simplificado) ou #grid (tipo coluna e linha)
#com o uso da função frame, podemos substituir o codigo acima por :
Label(frame, text='Para saber seu IMC digite os valores abaixo', pady=40).grid(column=1, row=1, columnspan=2)

'''
pady -> dar um espaçamento no eixo Y
padx -> espaçamento no eixo X
columnspan --> expande a coluna , colmo se mesclasse células do excel.
'''
Label(frame, text='Qual o seu peso (kg)?').grid(column=1, row=2)
peso = Entry(frame)
peso.grid(column=2, row=2)

Label(frame, text='Qual sua altura - separado por . (m)?').grid(column=1, row=3)
altura = Entry(frame)
altura.grid(column=2, row=3)

Button(frame, text='Calcular', command=calcula_imc).grid(column=2, row=4)
#command serve para fazer o botão chamar uma função 

resultado = Label(frame)
resultado.grid(column=1, row=5, columnspan=2)


janela.title('Calulcadora de IMC')
janela.mainloop()           #função que faz gerar a janela do final

