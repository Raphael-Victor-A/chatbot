import chatbot as cb
from tkinter import *


nomemaquina = "IAF1"
cb.saudacoes(nomemaquina)
while True:
    texto = cb.recebetexto()
    resposta = cb.buscaResposta(nomemaquina, texto)
    if cb.exibeResposta(resposta,nomemaquina) == "fim":
        break