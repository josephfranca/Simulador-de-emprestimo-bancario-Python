#  Simulador de Empréstimo com Histórico

Um aplicativo de desktop interativo desenvolvido em Python com a biblioteca **Tkinter**. Ele permite calcular o valor total e o valor das parcelas de um empréstimo com base em juros compostos, armazenando os resultados em um histórico visual dinâmico (tabela).

##  Funcionalidades

* **Cálculo de Juros Compostos:** Aplica de forma automatizada a fórmula de juros compostos a partir do valor principal, taxa e parcelas informadas.
* **Tabela de Histórico Dinâmica:** Utiliza o componente `Treeview` do Tkinter para listar e comparar múltiplas simulações lado a lado na mesma tela.
* **Gerenciamento de Dados:** Os dados são tratados inicialmente em dicionários (`Dict`) e organizados em uma lista (`List`) de simulações.
* **Limpeza de Histórico:** Opção de resetar e limpar tanto a memória interna do programa quanto as linhas visuais da tabela de forma simultânea.
* **Tratamento de Erros:** Evita o fechamento inesperado do programa caso o usuário digite letras ou caracteres inválidos nos campos numéricos.

---

##  Tecnologias Utilizadas

* **Python 3.x**
* **Tkinter & TTK** (Interface gráfica padrão e componentes avançados do Python)
* **Math** (Biblioteca nativa do Python utilizada para cálculos de potência)

---

## 📐 Lógica do Cálculo

O simulador utiliza o conceito financeiro de **Juros Compostos**, seguindo a fórmula matemática subjacente:

$$M = P \cdot (1 + i)^n$$

Onde:
* **M (Total Com Juros):** O montante final a ser pago.
* **P (Empréstimo):** O valor principal solicitado.
* **i (Taxa):** A taxa de juros mensal (convertida de porcentagem para decimal).
* **n (Parcelas):** O número total de meses/parcelas.

A partir do montante final ($M$), o aplicativo calcula o valor individual de cada parcela dividindo-o pela quantidade de meses ($n$).

---

##  Como Executar o Projeto

Como o Tkinter e a biblioteca Math já fazem parte da instalação padrão do Python, você não precisa instalar nenhuma dependência externa.

### Pré-requisitos
Certifique-se de possuir o Python 3 instalado no seu computador. Você pode fazer o download direto no site oficial [python.org](https://www.python.org/).

### Passo a Passo

1. **Clone o seu repositório:**
   ```bash
   git clone https://github.com/josephfranca/Simulador-de-emprestimo-bancario-Python.git
2. **Navegue até a pasta onde clonou o projeto:**
    
cd Quiz-Hist-ria-Brasileira
3. **Executando o projeto**
python "Simulador de emprestimo.py"
