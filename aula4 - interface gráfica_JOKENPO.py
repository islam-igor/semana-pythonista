import tkinter as tk
from tkinter import LEFT, Label, LabelFrame, Button, PhotoImage
import random

def jokenpo(escolha_usuário):
    escolha_computador = random.choice(['pedra', 'papel', 'tesoura'])

    if escolha_usuário ==  escolha_computador:
        mensagem = f'''
            Você: {escolha_usuário.upper()}
            PC: {escolha_computador.upper()}

            Resultado: EMPATE!
            '''
    elif (escolha_usuário == 'pedra' and escolha_computador == 'tesoura') \
            or (escolha_usuário == 'papel' and escolha_computador == 'pedra') \
            or (escolha_usuário == 'tesoura' and escolha_computador == 'papel'):
        
        mensagem = f'''
            Você: {escolha_usuário.upper()}
            PC: {escolha_computador.upper()}

            Resultado: VOCÊ GANHOU!
            '''
    elif (escolha_usuário == 'reset'):
        mensagem = ''

    else: 
        mensagem = f'''
            Você: {escolha_usuário.upper()}
            PC: {escolha_computador.upper()}

            Resultado: VOCÊ PERDEU!
            '''
    resultado.config(text=mensagem)

def escolheu_pedra():
    jokenpo(escolha_usuário='pedra')

def escolheu_papel():
    jokenpo(escolha_usuário='papel')

def escolheu_tesoura():
    jokenpo(escolha_usuário='tesoura')

def reset():
    jokenpo(escolha_usuário='reset')
    
janela = tk.Tk()

frame = LabelFrame(janela, text='Qual você escolhe?', padx=10, pady=10)
#LabelFrame cria uma janelinha pra encapsular os itens dentro dele
frame.pack()

icone_pedra = PhotoImage(file = r'images/pedra.png')
icone_papel = PhotoImage(file = r'images/papel.png')
icone_tesoura = PhotoImage(file = r'images/tesoura.png')
icone_jokenpo = PhotoImage(file = r'images/jokenpo.png')


Button(frame, text='Pedra', command=escolheu_pedra, image=icone_pedra, compound=tk.LEFT).grid(column=1, row=1, padx=5)
Button(frame, text='Papel', command=escolheu_papel, image=icone_papel, compound=tk.LEFT).grid(column=2, row=1, padx=5) 
Button(frame, text='Tesoura', command=escolheu_tesoura, image=icone_tesoura, compound=tk.LEFT).grid(column=3, row=1, padx=5)
Button(frame, command=reset, image=icone_jokenpo, compound=tk.LEFT).grid(column=0, row=0, columnspan=4)

resultado = Label(frame, pady=10, padx=10, justify=tk.LEFT)
resultado.grid(column=0, row=2, columnspan=3)
#criou o espaço para imprimir o resultado do jogo

#flaticon é um site para encontrar icones , você baixa e coloca na mesma pasta do programa

janela.title('JO - KEN - PO')
janela.geometry('500x300+500+200')  #indica os pixel de inicialização de uma janela quando criada
janela.mainloop()