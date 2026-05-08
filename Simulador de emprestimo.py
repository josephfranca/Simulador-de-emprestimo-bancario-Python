import tkinter as tk
from tkinter import ttk
import math

#Criando array pra fazer e manipular o histórico
historico_simulacoes = []

def calculo():
    try:
        valorPrincipal = float(valorEmprestimo_entrada.get())
        valorTaxa = float(taxaEmprestimo_entrada.get()) / 100
        valorParcelas = int(parcelas_entrada.get()) 
        
        valorTotal = valorPrincipal * math.pow(1 + valorTaxa, valorParcelas)
        valorParcela = valorTotal / valorParcelas
        
        #Criando um dicionário que vai ser usado para tratar os dados e organizar antes de ir para o array
        dados_simulacao = {
            "principal": valorPrincipal,
            "taxa": valorTaxa * 100,
            "qtd_parcelas": valorParcelas,
            "total": valorTotal,
            "parcela": valorParcela
        }
        
        #Adicionando as chaves e dados do dicionário no array 
        historico_simulacoes.append(dados_simulacao)
        
        #Inserindo as chaves e dados na tabela visual
        tabelaExibicao.insert("", "end", values=(
             f"R$ {dados_simulacao['principal']:.2f}", 
             f"{dados_simulacao['taxa']:.1f}%", 
             f"{dados_simulacao['qtd_parcelas']}x", 
             f"R$ {dados_simulacao['total']:.2f}",
             f"R$ {dados_simulacao['parcela']:.2f}"
        ))
        
    except ValueError:  
        print("Digite somente números válidos nos campos.")

#Criando a função para limpar o histórico salvo na array
def limpar_historico():
    # Limpa a estrutura de dados (Lista)
    historico_simulacoes.clear()
    #Laço for usado para apagar visualmente a tabela, o tkinter não tem um comando para deletar todos de uma vez, então precisa ir deletando individualmente
    #get_children pega os id de cada linha
    for i in tabelaExibicao.get_children():
        tabelaExibicao.delete(i)

#Criando interface gráfica
janela = tk.Tk()
janela.title("Calculadora de empréstimo")
janela.geometry("650x500")

#Criando os inputs e usando o Entry para capturar os valores dos inputs
tk.Label(janela, text="Digite o valor do empréstimo:").pack()
valorEmprestimo_entrada = tk.Entry(janela)
valorEmprestimo_entrada.pack()

tk.Label(janela, text="Taxa mensal (%):").pack()
taxaEmprestimo_entrada = tk.Entry(janela)
taxaEmprestimo_entrada.pack()

tk.Label(janela, text="Quantidade de parcelas:").pack()
parcelas_entrada = tk.Entry(janela)
parcelas_entrada.pack()

#Criando os botões
frameBotoes = tk.Frame(janela)
frameBotoes.pack(pady=10)

#Configurando e linkando a função nos botões
botaoCalcular = tk.Button(frameBotoes, text="Calcular", command=calculo, bg="lightgreen")
botaoCalcular.pack(side="left", padx=5)

botaoLimpar = tk.Button(frameBotoes, text="Limpar Tudo", command=limpar_historico, bg="salmon")
botaoLimpar.pack(side="left", padx=5)

#Criando a tabela
frameResultado = tk.Frame(janela)
frameResultado.pack(pady=10)
#Criando a estrutura das colunas e seus títulos
colunas = ("Empréstimo", "Taxa", "Parcelas","Total Com Juros", "mensal")
tabelaExibicao = ttk.Treeview(frameResultado, columns=colunas, show="headings")

#Usando o laço for para preencher as colunas
for col in colunas:
    tabelaExibicao.heading(col, text=col.capitalize())
    tabelaExibicao.column(col, width=110, anchor="center")

tabelaExibicao.pack()

janela.mainloop()