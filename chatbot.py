def saudacaoGUI(nome):
    import random
    frases = ["Bom dia , meu nome é" +nome+"Como vai você hoje?" , "tudo bem?"]
    print(frases[random.randint(0,2)])

def salvaSugestao(sugestao):
    with open("baseConhecimento.txt", "a+") as conhecimento:
        conhecimento.write("Chatbot: "+ sugestao+"\n")

def buscaRespostaGUI(texto):
    with open("baseConhecimento.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if jaccard(texto, viu) > 0.3:
                    proximaLinha = conhecimento.readline()
                    if "Chatbot: " in proximaLinha:
                        return proximaLinha
            else:
                conhecimento.write('\n' + texto)
                return "Me desculpe, não sei oque falar"
                    
def jaccard(textoUsuario, textoBase):
    textoUsuario = limpaFrase(textoUsuario)
    textoBase = limpaFrase(textoBase)
    if len(textoBase)< 1: return 0
    else:
        palavrasEmComum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavrasEmComum +=1
            return palavrasEmComum/(len(textoBase.split()))
            
def limpaFrase(frase):
    tirar = ["?", "!", "...", ".", ",", ":", "Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase



def exibeRespostaGUI(texto,resposta,nome):
    return resposta.replace("Chatbot",nome)
   

                        