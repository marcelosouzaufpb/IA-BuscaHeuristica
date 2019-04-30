textoSeparadoLinha = []
textoSeparadoPalavras = []
fraseSeparada = []
palavrasBi =[]
palavrasTri = []

def separaPalavra():
    for palavra in range(textoSeparadoLinha.count()):
        textoSeparadoPalavras.append(palavra)

def bigrama(palavraAtual, palavraAnterior):
    probabilidade = contadorDoBigrama(palavraAtual, palavraAnterior)/contadoDePalavras(palavraAtual)
    return probabilidade

def trigrama(palavraAtual, palavraAnterior1, palavraAnterior2):
    probabilidade = contadorDoTrigrama(palavraAtual, palavraAnterior1, palavraAnterior2)/contadorDoBigrama(palavraAnterior1,palavraAnterior2)
    return probabilidade

def contadoDePalavras(palavraAtual):
    cont = 0
    for linhas in textoSeparadoLinha:
        for palavraIterada in linhas:
            if(palavraIterada == palavraAtual):
                cont = cont+1
    return cont

def contadorDoBigrama(palavraAtual, palavraAnterior):
    cont = 0
    for linhas in textoSeparadoLinha:
        for palavraIterada in linhas:
            if(palavraIterada == palavraAtual):
                if(encontraPalavraAnterior(palavraIterada)==palavraAnterior):
                    cont = cont+1
    return cont

def contadorDoTrigrama(palavraAtual, palavraAnterior1, palavraAnterior2):
    cont = 0
    for linhas in textoSeparadoLinha:
        for palavraIterada in linhas:
            if(palavraIterada == palavraAtual):
                if(encontraPalavraAnterior(palavraIterada.index())==palavraAnterior1):
                    if(encontraPalavraAnterior(encontraPalavraAnterior(palavraIterada.index())) ==palavraAnterior2):                    
                        cont = cont+1 
    return cont

def encontraPalavraAnterior(index):
    return textoSeparadoLinha[index-1]

def lerTxt(diretorio):
    arquivoLido = open(diretorio, 'r')
    arquivoSeparadoEmLinhas = arquivoLido.readlines()
    for linhas in arquivoSeparadoEmLinhas:
        linhasEditadas = linhas.split(" ")
        textoSeparadoLinha.append(linhasEditadas)
    
def injetaFrase(frase):
    palavrasDaFrase = frase.split(" ")
    fraseSeparada.append(palavrasDaFrase)

def calculaProbabilidadeBi():
    prob = 1
    prob*=contadoDePalavras(fraseSeparada[0]) 
    indexAtual = 1
    for palavra in range(1, fraseSeparada.count(),1):
       prob*=bigrama(palavra,fraseSeparada[indexAtual-1])
       indexAtual= indexAtual+1
    return prob
def calculaProbabilidadeTri():
    prob = 1
    prob*=contadoDePalavras(fraseSeparada[0]) 
    indexAtual = 1
    prob*=bigrama(fraseSeparada[indexAtual],fraseSeparada[indexAtual+1])
    indexAtual= indexAtual+1
    for palavra in range(2, fraseSeparada.count(),1):
       prob*=trigrama(palavra,fraseSeparada[indexAtual-1],fraseSeparada[indexAtual-2])
       indexAtual= indexAtual+1
    return prob
def addPalavra(palavra):
    fraseSeparada.append(palavra);

def probPalavraBi(palavra):
    addPalavra(palavra)
    prob1 = calculaProbabilidadeBi()
    return prob1

def probPalavraTri(palavra):
    addPalavra(palavra)
    prob2 = calculaProbabilidadeBi()
    return prob2

def removeElemento(palavra):
    for palavraTeste in range (textoSeparadoPalavras):
        if(palavraTeste ==  palavra):
            textoSeparadoPalavras.remove(palavra)

def palavrasPossiveisBi():
    palavraMaiorProb = probPalavraBi(textoSeparadoPalavras[0])
    palavra1 = ""
    palavra2 = ""
    palavra3 = ""
    palavras = []
    
    for palavra in textoSeparadoPalavras:
        testeMaiorProb = probPalavraBi(palavra)
        if(palavraMaiorProb < testeMaiorProb):
            palavraMaiorProb = testeMaiorProb
            palavra1=palavra
    removeElemento(palavra1)
    
    for palavra in range(textoSeparadoPalavras):
        testeMaiorProb = probPalavraBi(palavra)
        if(palavraMaiorProb < testeMaiorProb):
            palavraMaiorProb = testeMaiorProb
            palavra2 = palavra
    removeElemento(palavra2)
    for palavra in range(textoSeparadoPalavras):
        testeMaiorProb = probPalavraBi(palavra)
        if(palavraMaiorProb < testeMaiorProb):
            palavraMaiorProb = testeMaiorProb
            palavra3 = palavra
    removeElemento(palavra3)
    palavras.append(palavra1)
    palavras.append(palavra2)
    palavras.append(palavra3)
    return palavras

def palavrasPossiveisTri():
    palavraMaiorProb = probPalavraTri(textoSeparadoPalavras[0])
    palavra1 = ""
    palavraMaiorProb2 = probPalavraTri(textoSeparadoPalavras[0])
    palavra2 = ""
    palavraMaiorProb2 = probPalavraTri(textoSeparadoPalavras[0])
    palavra3 = ""
    palavras = []
    
    for palavra in textoSeparadoPalavras:
        testeMaiorProb = probPalavraTri(palavra)
        if(palavraMaiorProb < testeMaiorProb):
            palavraMaiorProb = testeMaiorProb
            palavra1=palavra
    removeElemento(palavra1)
    
    for palavra in range(textoSeparadoPalavras):
        testeMaiorProb = probPalavraTri(palavra)
        if(palavraMaiorProb < testeMaiorProb):
            palavraMaiorProb = testeMaiorProb
            palavra2 = palavra
    removeElemento(palavra2)
    for palavra in range(textoSeparadoPalavras):
        testeMaiorProb = probPalavraTri(palavra)
        if(palavraMaiorProb < testeMaiorProb):
            palavraMaiorProb = testeMaiorProb
            palavra3 = palavra
    removeElemento(palavra3)
    palavras.append(palavra1)
    palavras.append(palavra2)
    palavras.append(palavra3)
    return palavras

    
def run():
    lerTxt("texto.txt")
    injetaFrase("Olá meu amigo")
    print("Olá meu amigo")
    print(palavrasPossiveisBi())
    print(palavrasPossiveisTri())

run()