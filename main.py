from categoria import Categoria
from transacao import Transacao
import customtkinter
from customtkinter import *
import os


root = customtkinter.CTk()
root.geometry('800x400')
root.title("Finanças")


fonte = customtkinter.CTkFont("JetBrains Mono", size=12)

usuario = os.getlogin()

nome = customtkinter.CTkLabel(root, text= f"Olá, {usuario} ", font = ('JetBrains Mono', 16))
nome.place(x=30, y= 35)


eu = []

def adicionar():
    root2 = customtkinter.CTkToplevel()
    root2.geometry("300x320")
    
    lb = customtkinter.CTkLabel(root2, text="Qual valor?", font=fonte)
    lb.place(relx=0.5, y=20, anchor="center")
    
    lb2 = customtkinter.CTkLabel(root2, text="Qual a descrição?", font=fonte)
    lb2.place(relx=0.5, y=90, anchor="center")
    
    lb3 = customtkinter.CTkLabel(root2, text="Qual Categoria?", font=fonte)
    lb3.place(relx=0.5, y=200, anchor="center")
    
    en = customtkinter.CTkEntry(root2)
    en.place(x=90, y=35) 
    
    en2 = customtkinter.CTkEntry(root2)
    en2.place(x=90, y=105) 
    
    conta_fixa = Categoria.CONTA_FIXA.name
    gastos = Categoria.DESPESA.name
    receita = Categoria.RECEITA.name
    
    opcoes = [conta_fixa, gastos, receita]
    var = customtkinter.StringVar(root2)
    var.set(opcoes[0]) 
    
    en3 = customtkinter.CTkOptionMenu(root2, variable=var, values=opcoes)
    en3.place(x=150, y=235, anchor="center") 

    def acionar():
        try:
            va = float(en.get())
        except ValueError:
            error_label = customtkinter.CTkLabel(root2, text="Por favor, insira um valor numérico", font=fonte, fg_color="red")
            error_label.place(relx=0.5, y=170, anchor="center")
            return
        
        de = en2.get()
        ca = en3.get()
        
        
        if ca == Categoria.DESPESA.name:
            va = -abs(va)
        
        transacao = Transacao(va, de, Categoria[ca])
        eu.append(transacao)
        
        def total_total():
            contador = 0
            for t in eu:
                contador += t.getvalor()
            return contador
            
        saldoConta.configure(text=f"SALDO: {total_total()}")
        tran_text = "\n".join([f"DESCRIÇÃO: {t.descricao} / VALOR: {t.valor} / CATEGORIA: {t.categoria.name}" for t in eu])
        tran.configure(text=f"Transações Realizadas: \n{tran_text}")
        root.update()
        root2.destroy()

    botao = customtkinter.CTkButton(root2, text="Adicionar Transação", command=acionar)
    botao.place(relx=0.5, y=280, anchor="center")

    root2.mainloop()


saldoConta = customtkinter.CTkLabel(root, text="SALDO: 0", font=("JetBrains Mono", 16))
saldoConta.place(x=620, y=35)

tran = customtkinter.CTkLabel(root, text="Transações Realizadas:", font=fonte)
tran.place(relx=0.5, y=180, anchor="center")

bt = customtkinter.CTkButton(root, text="Adicionar RECEITA/GASTOS/LAZER", font=fonte, command=adicionar)
bt.place(relx=0.5, y=350, anchor="center")

root.mainloop()
