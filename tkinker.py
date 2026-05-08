import tkinter as tk #importando tkinter e abreviando


# nome = input("Digite seu nome: ")

janela = tk.Tk() #criando janela baseado na variável janela
janela.title("título") #Criando o titulo da janela
janela.geometry("400x300") #Definindo tamanho


# tk.Label(janela,text=f"Bem vindo").pack() #Primeiro argumento é qual janela ele vai aparecer e o segundo é o texto, precisa do pack pra aparecer
texto = tk.Label(janela,text=f"Bem vindo")
texto.pack()

# def respostaBotao():
#     print("Olá")

def respostaBotao():
    nome = entradaTexto.get() #pegando o valor do input
    texto['text'] = f"Olá, {nome}" # dessa forma ele muda o texto na parte de cima da janela, abaixo do título
    
entradaTexto = tk.Entry(janela) #Criando o input, porém ainda precisa usar o pack para adicionar na janela
entradaTexto.pack()

botao = tk.Button(janela, text="Botão teste", command=respostaBotao).pack() #Mesmo esquema do label, command para chamar a função

janela.mainloop()

#Esse arquivo foi criado apenas para estudar a biblioteca Tkinker e como ela funciona