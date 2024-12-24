import pandas as pd
import os

# coletando os dados do dataset de personagens
filePath = "./engine/BibleData-PersonVerseTanakh.csv"
dataFrame = pd.read_csv(filePath)

indexData = dataFrame['index']
personVerseIdData = dataFrame['person_verse_id']
referenceData = dataFrame['reference_id']
personLabelIdData = dataFrame['person_label_id']
personIdData = dataFrame['person_id']
personLabelData = dataFrame['person_label']
personLabelCountData = dataFrame['person_label_count']
personVerseSequenceData = dataFrame['person_verse_sequence']
personVerseNotesData = dataFrame['person_verse_notes']


# coletando dados do dataset de texto (.json)
dataFrameTexto = pd.read_json("./engine/nvi.json", encoding="utf-8-sig")
CAPITULOS = dataFrameTexto['chapters'][:39]
NOMES = dataFrameTexto['name'][:39]

# funções de contagem
def Capitulos():
    arrayBooks = referenceData.array
    finalArray = []

    for item in arrayBooks:
        if(item[5] == ':'):
            finalArray.append(item[:6])
        else:
            finalArray.append(item[:7])

    total = pd.Series(finalArray)
    return total

def Livros():
    arrayBooks = referenceData.array
    finalArray = []

    for item in arrayBooks:
        finalArray.append(item[:3])

    total = pd.Series(finalArray)
    return total

def LivrosNome():
    capitulos = Capitulos().unique()

    item = 0
    listaCapitulo = []

    while(item < len(capitulos)):
        livro = ''
        sub = 0
        letra = capitulos[item][sub]
        while(letra != ' '):
            livro += letra
            sub+=1
            letra = capitulos[item][sub]
        item+=1
        listaCapitulo.append(livro)
    
    return listaCapitulo

#pega o nome do livro em portugues
def ConversorLivro(arg: str):
    caps = pd.Series(LivrosNome()).unique()

    indice = 0

    while(arg != caps[indice]):
        indice+=1
    
    return NOMES[indice]


# funções de busca totais
def totalVersiculos():
    total = len(indexData) #total de itens dentro de indexData
    return total

def totalPersonagem():
    person = personIdData.unique()
    total = len(person)
    return total

def totalLivros():
    livros = Livros().unique()
    total = len(livros)
    return total

def totalCapitulos():
    capitulos = Capitulos().unique()
    total = len(capitulos)
    return total

#funções estatisticas
def mediaCapitulos():
    capitulos = totalCapitulos()
    livros = totalLivros()
    total = capitulos/livros
    return total

def mediaVersiculos():
    versiculos = totalVersiculos()
    capitulos = totalCapitulos()
    total = versiculos/capitulos
    return total

def mediaVersiculosLivro():
    versiculos = totalVersiculos()
    livros = totalLivros()
    total = versiculos/livros
    return total

def mediaPersonagensCapitulo():
    personagens = totalPersonagem()
    capitulos = totalCapitulos()
    media = personagens/capitulos
    return media

def mediaPersonagensLivro():
    personagens = totalPersonagem()
    livros = totalLivros()
    media = personagens/livros
    return media

#recebe uma posição
def maisCitado(arg = 0):
    personagens = personIdData.value_counts()
    resultado = personagens.index[arg][:-2]
    return resultado

#recebe uma posição
def menosCitado(arg):
    if(arg > 0):
        arg = arg * -1
    elif(arg == 0):
        arg = -1

    return maisCitado(arg)

#recebe uma posição
def maisCapitulo(indice = 0):
    listaCapitulo = LivrosNome()
    
    total = pd.Series(listaCapitulo).value_counts()
    resposta = total.index[indice]

    return ConversorLivro(resposta)

#recebe uma posição
def menosCapitulo(indice):
    if(indice > 0):
        indice = indice* -1
    elif(indice == 0):
        indice = -1

    return maisCapitulo(indice)

def enderecoLivro(livro=1,cap=1,vers=1):
    livro = NOMES[livro-1]
    capitulo = cap-1
    versiculo = vers-1

    retorno = f"{livro} {capitulo}:{versiculo}"
    return retorno

def capituloEspecifico(livro=1,cap=1):
    livros = [item for item in CAPITULOS[livro-1]]
    capitulo = [item for item in livros[cap-1]]

    return capitulo

def versiculoEspecifico(livro=1,cap=1,vers=1):
    capitulo = capituloEspecifico(livro,cap)
    versiculo = capitulo[vers-1]
    return versiculo

def totalCapitulosLivro(nome: str):
    indice = 0
    
    while(str(NOMES[indice]).lower() != nome.lower()):
        indice+=1

    total = len(CAPITULOS[indice])

    return total

def totalVersiculosLivro(nome: str):
    indice = 0

    while(str(NOMES[indice]).lower() != nome.lower()):
        indice+=1
    
    total = 0
    
    for item in CAPITULOS[indice]:
        total += len(item)
    return total