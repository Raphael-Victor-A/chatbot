import chatbot as cb
from tkinter import *


main_window = Tk()

main_window.title("Chatbot")
main_window.geometry("500x700")
main_window.grid()

frame = Frame(main_window)
frame.grid()

labelIdentificacao = Label(frame, text = "Insira uma mensagem aqui: ")
labelIdentificacao.grid(row=0, column=0)

entradaMensagem = Entry(frame)
entradaMensagem.grid(row=0, column=1)

frame2 = Frame(main_window)
frame2.grid(row=1,column=0)
historico = StringVar()
Label(frame2, textvariable=historico).grid()

nomeMaquina = "Chatbot"
historico.set("Qual seu nome? ")

entradaSugestao = False
entradaNomeUsuario = True
nomeUsuario = ""

def rodaChatbot():
    global entradaSugestao
    global entradaNomeUsuario
    global historicoConversa
    global nomeUsuario
    global nomeMaquina

    if entradaNomeUsuario:
        nomeUsuario = entradaMensagem.get()
        saudacao = cb.saudacaoGUI(nomeMaquina)
        historicoConversa = nomeMaquina+ ": " + saudacao + "\n"
        historico.set(historicoConversa)
        entradaNomeUsuario = False
    else:
        texto = entradaMensagem.get()
        historicoConversa += "\n"+ nomeUsuario + ": " + texto
        historico.set(historicoConversa)

        if entradaSugestao:
            cb.salvaSugestao(texto)
            entradaSugestao = False
            historicoConversa += "\n Agora aprendi, vamos continuar a conversa...\n"
            historico.set(historicoConversa)

        else:
            resposta = cb.buscaRespostaGUI("Cliente: "+texto+"\n")
            if resposta == "Me desculpe, não sei oque falar":
                historicoConversa += "\n Me desculpe. Oque voce esperava? \n"
                entradaSugestao = True
            else:
                historicoConversa += "\n"+cb.exibeRespostaGUI(texto,resposta,nomeMaquina)
                historico.set(historicoConversa)

Button(frame,text="Clique", command=rodaChatbot).grid(row=0, column=2)
main_window.mainloop()