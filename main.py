from categoria import Categoria
from transacao import Transacao
import customtkinter 
from customtkinter import *

eu = Transacao()

root = customtkinter.CTk()
root.geometry('400x400')
root.title("Finanças")

label1 = customtkinter.CTkLabel(root, text = f"SALDO: {eu.valor}")
label1.place(x=10,y=20)

bt = customtkinter.CTkButton(root, text="Adicionar RECEITA/GASTOS/LAZER")
bt.place(x=100, y=200)

root.mainloop()