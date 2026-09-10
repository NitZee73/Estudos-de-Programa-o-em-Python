import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as ms
from tkinter.ttk import Combobox

# Criacao das listas de servicos e precos

servicos = ['Formatação', 'Limpeza preventiva', 'Instalação de software', 'Backup de arquivos', 'Diagnóstico']

precos = {'Formatação': 100, 'Limpeza preventiva': 80, 'Instalação de software': 50, 'Backup de arquivos': 70, 'Diagnóstico': 60}

# criacao da janela

janela = tk.Tk()

janela.title('Orçamento de Assistencia Técnica')

janela.geometry('550x500')

# Criacao do titulo

titulo = tk.Label(janela, text='Orçamento de Assistência Técnica', font=('Arial', 16, 'bold'))

titulo.pack(pady=10)

# criacao do frame dos campos

frame = tk.Frame(janela)

frame.pack(pady=10, fill='x')

# criacao do label cliente

label_cl = tk.Label(frame, text='Cliente:', font=('Arial', 12))

label_cl.grid(row=0, column=0, sticky='w')

# criacao do entry cliente

campo_cl = tk.Entry(frame, width=40)

campo_cl.grid(row=0, column=1, sticky='w', padx=55)

# criacao do label servico

label_sr = tk.Label(frame, text='Serviço:', font=('Arial', 12))

label_sr.grid(row=1, column=0, sticky='w')

# criacao do COMBOBOX servico

campo_sr = ttk.Combobox(frame, value=servicos, width=37, state='readonly')

campo_sr.grid(row=1, column=1, padx=55, sticky='w')

# funcao de validacao da quantidade

def validar_numero(valor):
    return valor.isdigit() or valor == ''

validacao = janela.register(validar_numero)

# criacao do label quantidade

label_qt = tk.Label(frame, text='Quantidade:', font=('Arial', 12))

label_qt.grid(row=2, column=0, sticky='w')

# criacao do entry quantidade

campo_qt = tk.Entry(frame, width=40, validate='key', validatecommand=(validacao, '%P'))

campo_qt.grid(row=2, column=1, padx=55, sticky='w')

# criacao do checkbutton urgencia

urgente = tk.BooleanVar()

campo_urg = tk.Checkbutton(janela, text='Serviço urgente', variable=urgente)

campo_urg.pack()

# criacao da funcao de calculo e salvamento de informacoes

def calc_os():

    cliente = campo_cl.get()

    servico = campo_sr.get()

    quantidade_texto = campo_qt.get()

    urgencia = urgente.get()

    # validacao dos campos para que nao fiquem vazios

    if cliente == '' or servico == '' or quantidade_texto == '':
        ms.showerror('Erro', 'Preencha todos os campos corretamente.')
        return

    quantidade = int(quantidade_texto)

    # validacao da quantidade para que seja maior que zero

    if quantidade <= 0:
        ms.showerror('Erro', 'A quantidade deve ser maior que zero.')
        return

    # calculo do preco total

    preco = precos[servico]

    total = preco * quantidade

    # aplicacao da taxa de urgencia

    if urgencia is True:
        total += total * 0.2

    # configuracao dos labels de resumo

    label_res_cl.config(text=f'Cliente: {cliente}')

    label_res_sr.config(text=f'Serviço: {servico}')

    label_res_qt.config(text=f'Quantidade: {quantidade}')

    label_res_urg.config(text=f'Urgência: {"Sim" if urgencia else "Não"}')

    resultado_preco.config(text=f'Valor unitário: R$ {preco:.2f}')

    label_result.config(text=f'Valor total: R$ {total:.2f}')

    # limpeza dos campos apos o calculo

    campo_cl.delete(0, tk.END)

    campo_sr.set('')

    campo_qt.delete(0, tk.END)

    urgente.set(False)

# Criacao botao calcular

bt_cal = tk.Button(janela, text='Calcular', command=calc_os)

bt_cal.pack(pady=10)

# criacao do frame do resumo

frame_resum = tk.Frame(janela)

frame_resum.pack(pady=10, fill='x')

# criacao do titulo do frame de resumo

tit_resul = tk.Label(frame_resum, text='Resumo do Orçamento', font=('Arial', 14, 'bold'))

tit_resul.pack(pady=10)

# criacao do label resumo cliente

label_res_cl = tk.Label(frame_resum, text='Cliente:', font=('Arial', 12))

label_res_cl.pack(anchor='w', padx=10)

# criacao do label resumo servico

label_res_sr = tk.Label(frame_resum, text='Serviço:', font=('Arial', 12))

label_res_sr.pack(anchor='w', padx=10)

# criacao do label resumo quantidade

label_res_qt = tk.Label(frame_resum, text='Quantidade:', font=('Arial', 12))

label_res_qt.pack(anchor='w', padx=10)

# criacao do label resumo urgencia

label_res_urg = tk.Label(frame_resum, text='Urgência:', font=('Arial', 12))

label_res_urg.pack(anchor='w', padx=10)

# criacao do label preco unitario

resultado_preco = tk.Label(frame_resum, text='Valor unitário:', font=('Arial', 12))

resultado_preco.pack(anchor='w', padx=10)

# criacao do label preco total

label_result = tk.Label(frame_resum, text='Valor total:', font=('Arial', 12))

label_result.pack(anchor='w', padx=10)

janela.mainloop()