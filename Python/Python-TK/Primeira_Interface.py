import tkinter as tk
from tkinter import ttk
from tkinter import ttk, messagebox
#Criação da lista de usuários
cadastros = []
#Criação da janela
janela = tk.Tk()
janela.title("Cadastro de Usuário")
janela.geometry("700x500")
#Criação do título
titulo = tk.Label(janela, text = 'Sistema de Cadastro', font = ("Arial" , 18))
titulo.pack(pady = 20)
#Criação do frame
frame_form = tk.Frame(janela)
frame_form.pack(pady = 10)
#Criação do Label nome
label_nome = tk.Label(frame_form, text='Nome:')
label_nome.grid(row=0, column=0)
#Criação do Entry nome
campo_nome = tk.Entry(frame_form, width=40) 
campo_nome.grid(row=0, column=1)
#Criação do Label email
label_mail = tk.Label(frame_form, text='E-mail:')
label_mail.grid(row=1, column=0)
#Criação do Entry email
campo_mail = tk.Entry(frame_form, width=40) 
campo_mail.grid(row=1, column=1)
#Criação do Label telefone
label_tel = tk.Label(frame_form, text='Telefone:')
label_tel.grid(row=2, column=0)
#Criação do Entry telefone
campo_tel = tk.Entry(frame_form, width=40) 
campo_tel.grid(row=2, column=1)
#Criação do Label de registros
label_regi = tk.Label(janela, text = 'Cadastros realizados', font=('Arial', 14)) 
label_regi.pack(pady=10)
#Criação da Treeview
tabela = ttk.Treeview(janela, columns=("nome", "email", "telefone"), show="headings")
#Nomeação dos cabeçalhos
tabela.heading('nome', text='Nome')
tabela.heading('email', text='E-mail')
tabela.heading('telefone', text='Telefone')
#Definição do tamanho das colunas
tabela.column('nome',width=180)
tabela.column('email',width=250)
tabela.column('telefone',width=180)
tabela.pack(pady=10)
#Criação da Função de salvamento
def save_cad():
    nome = campo_nome.get()
    email = campo_mail.get()
    telefone = campo_tel.get()
    if nome == "" or email == "" or telefone == "":
        messagebox.showwarning("Verifique os campos", "Todos os campos devem ser preenchidos!")
        return
    registro = [nome,email,telefone] 
    cadastros.append(registro)
    tabela.insert("", "end", values=(nome, email, telefone))
    campo_nome.delete(0, tk.END)
    campo_mail.delete(0, tk.END)
    campo_tel.delete(0, tk.END)
    messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
#Criação do botão de salvar
bot_save = tk.Button(janela, text= 'Salvar cadastro', command=save_cad)
bot_save.pack(pady=10)





















janela.mainloop()