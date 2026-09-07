import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as ms
from tkinter.ttk import Combobox
#Criacao das listas de servicos e precos
servicos = ['Formatação', 'Limpeza preventiva', 'Instalação de software', 'Backup de arquivos', 'Diagnóstico']
precos = {'Formatacao': 100, 'Limpeza preventiva': 80, 'Instalação de software': 50, 'Backup de arquivos': 70, 'Diagnóstico': 60}
#criacao da janela
janela=tk.Tk()
janela.title = ('Orçamento de Assistencia Técnica')
janela.geometry('550x500')
#Criacao do titulo
titulo=tk.Label(janela, text='Orçamento de Assistência Técnica', font=('Arial', 16, 'bold'))
titulo.pack(pady=10)
#criacao do campo cliente
frame=tk.Frame(janela)
frame.pack(pady=10)
#criacao do label cliente
label_cl=tk.Label(frame, text='Cliente:', font=('Arial', 12))
label_cl.grid(row=0,column=0, padx=10)
#criacao do entry cliente
campo_cl = tk.Entry(frame, width = 40)
campo_cl.grid(row=0,column=1, padx=10)
#criacao do label servico
label_sr=tk.Label(frame, text='Serviço:', font=('Arial', 12))
label_sr.grid(row=1,column=0)
#criacao do COMBOBOX servico
campo_sr=ttk.Combobox(frame, value=servicos, width=37)
campo_sr.grid(row=1,column=1, padx=10)
#criacao do entry quantidade
label_qt=tk.Label(frame, text='Quantidade:', font=('Arial', 12))
label_qt.grid(row=2,column=0)
#criacao do entry quantidade
campo_qt=tk.Entry(frame, width=40)
campo_qt.grid(row=2,column=1, padx=10)
#criacao do label urgencia
label_urg=tk.Label(frame, text='Urgência:', font=('Arial', 12))
label_urg.grid(row=3,column=0)
#criacao do combobox urgencia
campo_urg=ttk.Combobox(frame, value=['Baixa','Média','Alta'], width=37)
campo_urg.grid(row=3,column=1, padx=10)
#criacao da funcao de caulculo e salvamento de incformacoes
def calc_os():
    cliente = campo_cl.get()
    servico = campo_sr.get()
    quantidade = int(campo_qt.get())
    precos = precos[servico]
    total = precos * quantidade

#Criacao botao calcular
bt_cal=tk.Button(janela, text='Calcular', command=calc_os)
bt_cal.pack(pady=10)






















janela.mainloop()