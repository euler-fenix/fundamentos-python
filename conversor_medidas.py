#Desenvolva um código utilizando seus conhecimentos de Tkinter para converter uma unidade de medida de centímetros para metros.

import tkinter as tk

def converter_cm_m():
    try:
        centimetros = float(input_cm.get())
        metros = centimetros / 100  #conversao para metros
        
        label.config(text=f"{float(input_cm.get()):.2f} cm, convertidos em metros é: {metros:.2f} m")
    except ValueError:
        label.config(text='Valor invalido! \nPor favor, informe um valor valido!')

# janela principal
janela = tk.Tk()
janela.title('Conversor de Centimetros para Metros')
janela.geometry('600x400')  # tamanho da janela: 600p x 400p

titulo = tk.Label(janela, text='Conversor de Centimetros para Metros', font=("Arial", 20))
titulo.pack(pady=10)

# informa o valor
label_centimetros = tk.Label(janela, text='Informe o valor em centimetros:', font=("Arial", 14))
label_centimetros.pack(pady=10)

# centimetros
input_cm = tk.Entry(janela, font=("Arial", 14))
input_cm.pack(pady=5)

# botao conversor
btn_converter = tk.Button(janela, text="Converter", command=converter_cm_m, font=("Arial", 14))
btn_converter.pack(pady=5)

#resultaod da conversao
label = tk.Label(janela, text="", font=("Arial", 14))
label.pack(pady=10)

janela.mainloop()
