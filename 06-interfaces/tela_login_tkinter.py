#Realize uma interface de login utilizando a biblioteca Tkinter em Python. 
# O objetivo é permitir que o usuário faça login somente se a senha tiver mais de 6 dígitos e se o e-mail contiver o caractere "@", 
# ou seja, realizar uma tela de login com restrições de e-mail e senha

from tkinter import *
from tkinter import messagebox

def login():
    email = input_email.get()
    senha = input_senha.get()
    msg = ''
    # Verifica senha com 6 caracteres e se possiu @
    if "@" not in email:
        msg += 'E-mail invalido, faltando "@". \n'
    if len(senha) < 6:
        msg += 'Senha deve conter 6 caracteres ou mais. \n'
    
        # Verificar erro na validacao
    if msg == '':
        messagebox.showinfo("Login", 'Login efetuado com sucesso!\n Bem vindo a Infinity')
        input_email.delete(0, END)
        input_senha.delete(0, END)
    else:
        messagebox.showerror("Login", f"e-mail ou senha incorretos!\n{msg}")

# janela
janela = Tk()
janela.geometry("800x400")
janela.title("Login Infinity")

#fundo vermelho para titulo
faixa_titulo = Frame(janela, bg="red", pady=5)
faixa_titulo.grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")

#Titulo na faixa vermelha
titulo = Label(faixa_titulo, text="INFINITY", font=("Arial", 24, "bold"), bg="red", fg="white")
titulo.pack()

# centralizar coluna
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

# e-mail
Label(janela, text="E-mail:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
input_email = Entry(janela, width=50, font=("Arial", 14))
input_email.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# senha
Label(janela, text="Senha:", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
input_senha = Entry(janela, show="*", width=50, font=("Arial", 14))
input_senha.grid(row=2, column=1, padx=10, pady=5, sticky="w")

#login
btn_login = Button(janela, text="Login", command=login, font=("Arial", 14))
btn_login.grid(row=3, column=0,columnspan=2 ,padx=10, pady=10, sticky=W)

janela.mainloop()

