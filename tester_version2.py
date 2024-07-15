from tkinter import *
from tkinter import ttk, messagebox
from tkscrolledframe import ScrolledFrame
from PIL import Image, ImageTk
import datetime

cor_fundo_claro = "#FFFFFF"
cor_fundo_escuro = "#2C2C2C"
cor_letra_claro = "#403d3d"
cor_letra_escuro = "#FFFFFF"

tema_atual = 'claro'

janela = Tk()
janela.title("Bot de Suporte")
janela.geometry('500x580')
janela.configure(background=cor_fundo_claro)
janela.resizable(width=False, height=False)

def mudar_tema():
    global tema_atual
    if tema_atual == 'claro':
        tema_atual = 'escuro'
        janela.configure(background=cor_fundo_escuro)
        frameCima.configure(bg=cor_fundo_escuro)
        frameMeio.configure(bg=cor_fundo_escuro)
        frameBaixo.configure(bg=cor_fundo_escuro)
        app_.configure(bg=cor_fundo_escuro)
        app_logo.configure(bg=cor_fundo_escuro, fg=cor_letra_escuro)
        frame_chat.configure(bg=cor_fundo_escuro)
        text_chat.configure(bg=cor_fundo_escuro, fg=cor_letra_escuro)
        entry_mensagem.configure(bg=cor_fundo_escuro, fg=cor_letra_escuro, insertbackground=cor_letra_escuro)
    else:
        tema_atual = 'claro'
        janela.configure(background=cor_fundo_claro)
        frameCima.configure(bg=cor_fundo_claro)
        frameMeio.configure(bg=cor_fundo_claro)
        frameBaixo.configure(bg=cor_fundo_claro)
        app_.configure(bg=cor_fundo_claro)
        app_logo.configure(bg=cor_fundo_claro, fg=cor_letra_claro)
        frame_chat.configure(bg=cor_fundo_claro)
        text_chat.configure(bg=cor_fundo_claro, fg=cor_letra_claro)
        entry_mensagem.configure(bg=cor_fundo_claro, fg=cor_letra_claro, insertbackground=cor_letra_claro)

def limpar_chat():
    text_chat.config(state=NORMAL)
    text_chat.delete(1.0, END)
    text_chat.config(state=DISABLED)

def enviar_mensagem():
    mensagem_usuario = entry_mensagem.get()
    if mensagem_usuario:
        adicionar_mensagem(mensagem_usuario, "Usuário")
        entry_mensagem.delete(0, END)
        resposta_bot(mensagem_usuario)

def adicionar_mensagem(mensagem, remetente):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    text_chat.config(state=NORMAL)
    text_chat.insert(END, f"{remetente} ({timestamp}): {mensagem}\n\n")
    text_chat.config(state=DISABLED)
    text_chat.yview(END)

def resposta_bot(mensagem_usuario):
    resposta = "Desculpe, não entendi a sua pergunta."
    if 'oi' in mensagem_usuario.lower() or 'olá' in mensagem_usuario.lower():
        resposta = "Olá! Como posso ajudar?"
    elif 'problema' in mensagem_usuario.lower():
        resposta = "Pode me dizer mais sobre o problema?"
    elif 'obrigado' in mensagem_usuario.lower() or 'obrigada' in mensagem_usuario.lower():
        resposta = "De nada! Fico feliz em ajudar."
    adicionar_mensagem(resposta, "Bot")

# Menu
menu_bar = Menu(janela)
janela.config(menu=menu_bar)

menu_opcoes = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Opções", menu=menu_opcoes)
menu_opcoes.add_command(label="Mudar Tema", command=mudar_tema)
menu_opcoes.add_command(label="Limpar Chat", command=limpar_chat)
menu_opcoes.add_separator()
menu_opcoes.add_command(label="Sair", command=janela.quit)

menu_ajuda = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)
menu_ajuda.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Bot de Suporte v1.0\nDesenvolvido por Você"))

# Frames
frameCima = Frame(janela, width=500, height=100, bg=cor_fundo_claro, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameMeio = Frame(janela, width=500, height=300, bg=cor_fundo_claro, relief="solid")
frameMeio.grid(row=1, column=0, sticky=NSEW)

frameBaixo = Frame(janela, width=500, height=300, bg=cor_fundo_claro, relief="flat")
frameBaixo.grid(row=1, column=0, sticky=NSEW)

# Imagem e Título
img_app = Image.open('imags/bot.png')
img_app = img_app.resize((70, 70))
img_app = ImageTk.PhotoImage(img_app)
app_ = Label(frameCima, height=70, image=img_app, compound=LEFT, anchor='center', bg=cor_fundo_claro)
app_.place(x=10, y=10)

app_logo = Label(frameCima, text="ChatBot de Suporte", compound=LEFT, padx=5, anchor=NW, font=('System 20 bold'), bg=cor_fundo_claro, fg=cor_letra_claro)
app_logo.place(x=100, y=20)

# ScrolledFrame
sf = ScrolledFrame(frameMeio, width=480, height=380)
sf.grid(row=1, column=0, sticky=NW)
sf.bind_arrow_keys(frameMeio)
sf.bind_scroll_wheel(frameMeio)
framecanva = sf.display_widget(Frame, bg=cor_fundo_claro)

frame_chat = Frame(framecanva, width=480, height=480, bg=cor_fundo_2, relief="flat")
frame_chat.grid(row=0, column=0, sticky=NSEW, padx=7, pady=10)

text_chat = Text(frame_chat, wrap=WORD, state=DISABLED, font=('Arial 10'), bg=cor_fundo_2, fg=cor_letra_claro)
text_chat.pack(expand=True, fill=BOTH)

entry_mensagem = Entry(frameBaixo, font=('Arial 12'), width=48, relief="solid")
entry_mensagem.grid(row=0, column=0, padx=10, pady=5)

button_imagem = Image.open('imgs/user.png'')
button_imagem = button_imagem.resize((30, 30))
button_imagem = ImageTk.PhotoImage(button_imagem)
button_enviar = Button(frameBaixo, image=button_imagem, command=enviar_mensagem, bg=cor_fundo_claro, relief=FLAT)
button_enviar.grid(row=0, column=1, padx=5, pady=5)

# Mensagens Iniciais
adicionar_mensagem("Olá! Como posso ajudar?", "Bot")

# Loop Principal
janela.mainloop()
