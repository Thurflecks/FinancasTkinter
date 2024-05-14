from categoria import Categoria
from transacao import Transacao
import customtkinter 
from customtkinter import *

eu = Transacao()

root = customtkinter.CTk()
root.geometry('400x400')
root.title("Finanças")
fonte = customtkinter.CTkFont("JetBrains 30")



def adicionar():
    root2 = customtkinter.CTkToplevel()
    root2.geometry("300x320")
    lb = customtkinter.CTkLabel(root2, text="Qual valor?", font=fonte)
    lb.place(relx=0.5, y=20, anchor="center")
    
    lb2 = customtkinter.CTkLabel(root2, text="Qual a descrição", font=fonte)
    lb2.place(relx=0.5, y=90, anchor="center")
    
    lb3 = customtkinter.CTkLabel(root2, text="Qual Categoria?", font=fonte)
    lb3.place(relx=0.5, y=200, anchor="center")
    
    en = customtkinter.CTkEntry(root2)
    en.place(x=90, y=35) 
    
    en2 = customtkinter.CTkEntry(root2)
    en2.place(x=90, y=105) 
    
    conta_fixa = Categoria.CONTA_FIXA.name
    gastos= Categoria.DESPESA.name
    receita = Categoria.RECEITA.name
    
    opcoes = [conta_fixa, gastos, receita]
    var = customtkinter.StringVar(root2)
    var.set(opcoes[0]) 
    
    en3 = customtkinter.CTkOptionMenu(root2, variable=var, values=opcoes)
    en3.place(x=90, y=215) 
    def acionar():
        va = float(en.get())
        de = en2.get()
        ca = en3.get()
        list = []
        eu.adc_valor(va,de,ca)
        list.append(eu)
        print(list)
        
        
    botao = customtkinter.CTkButton(root2, text="Adicionar Transação", command=acionar)
    botao.place(relx=0.5, y=280, anchor="center")
    
    
    
    
    
    root2.mainloop()

saldoConta = customtkinter.CTkLabel(root, text = f"SALDO: {eu.total_total()}", font=fonte)
saldoConta.place(relx=0.5,y=35, anchor="center")

tran = customtkinter.CTkLabel(root, text = f"Transações Realizadas: {list}", font=fonte)
tran.place(relx=0.5,y=60, anchor="center")


bt = customtkinter.CTkButton(root, text="Adicionar RECEITA/GASTOS/LAZER", font=fonte, command=adicionar)
bt.place(relx = 0.5, y=350, anchor="center")

root.mainloop()