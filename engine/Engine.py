from engine.Data import *
from random import choice

#Vetores de entradas
FASE0 = ['primeiro','segundo','terceiro','quarto','quinto','sexto','setimo','oitavo','nono']

FASE1 = ['qual','quem']
FASE1_1 = ['quantos','quantas']

FASE2 = ['personagem','pessoa','individuo','livro','capitulo','versiculo']
FASE2_2 = ['livros','capitulos','versiculos', 'personagens','pessoas']

FASE3 = ['mais','maior']
FASE3_5 = ['media','meio']
FASE4 = ['menos','menor']

FASE5 = [
    'aparece','apareceu','citado(a)','mencionado(a)','ocorreu',
    'tem','existe','existem','ha','aparecem','possui']

FASE6 = ['biblia','livro','capitulo', 'velho', 'versiculo']

FASE7 = [str(nome).lower() for nome in NOMES[:]]

#Dados complementares de saida
RefLivro = ['O livro','A escritura','O texto']
RefLivroConteudo = ['capitulos', 'conteudo','textos']
RefPersonagem = ['O personagem', "A pessoa", "O individuo", "Aquele"]
RefQuantidadePos = ['que mais','com mais','com maior']
RefQuantidadeNeg = ['que menos', 'com menos', 'com menor']
RefFrequencia = ['aparece','apareceu','foi citado','foi mencionado','foi visto','aparições','menções']
RefResposta = ['é','foi']
RefInicio = ['O','A']

#Dados de saida errada
RefErro = ['Não entendi sua pergunta','Tente reformular sua pergunta','Não consegui processar sua pergunta','Não entendi muito bem']

sinalizadorLivro = 0 #variavel global para indicar que um livro apareceu na busca
sinalizadorCapitulo = 0#indica que um capitulo apareceu na busca
sinalizadorVersiculo = 0#indica que um versiculo apareceu na busca
sinalizadorPersonagem = 0#indica que um personagem apareceu na busca

def prNota(arg: list):
    for item in arg:
        if(item == FASE1[1]):#nota maior para o termo 'quem'
            return 4
        if(item in FASE1):
            return 1
        
        if(item in FASE1_1):#nota maior para o termo 'quantos'
            return 10
    
    return 0

def sgNota(arg: list):
    for item in arg:
        if(item in FASE2_2): #plural
            if(item == FASE2_2[0]):#livros
                global sinalizadorLivro
                sinalizadorLivro = 1
                return 11
            if(item == FASE2_2[1]):#capitulos
                global sinalizadorCapitulo
                sinalizadorCapitulo = 1
                return 12
            if(item == FASE2_2[2]):#versiculos
                global sinalizadorVersiculo
                sinalizadorVersiculo = 1
                return 13
            if(item in FASE2_2[3:4]):
                return 14
            
        if(item in FASE2[3:]):#indica que a busca é sobre um conteudo (livro, capitulo, versiculo)
            return 8
        if(item in FASE2):
            global sinalizadorPersonagem
            sinalizadorPersonagem = 1
            return 5
        
    return 0

def trNota(arg: list):
    for item in arg:
        if(item in FASE3):#mais
            return 10
        if(item in FASE4):#menos
            return 2
    return 0

def qrNota(arg: list):
    for item in arg:
        if(item in FASE5[5:]):#existem
            return 12
        if(item in FASE5):#apareceu
            return 8
    return 0

def qnNota(arg: list):
    for item in arg:
        if(item == FASE6[0] or item == FASE6[3]):# biblia ou velho testamento
            return 1 
        if(item == FASE6[1]): #livro
            global sinalizadorLivro
            sinalizadorLivro = 1
            return 2
        if(item == FASE6[2]): #capitulo
            global sinalizadorCapitulo
            sinalizadorCapitulo = 1
            return 3   
        if(item == FASE6[4]):
            global sinalizadorVersiculo
            sinalizadorVersiculo = 1
            return 4     
    return 0

def sxNota(arg: list):
    for item in arg:
        if(item in FASE7):
            global sinalizadorLivro
            sinalizadorLivro = 1
            return [6,item]
    return [0]

def notaExtra(arg: list):
    for item in arg:
        if(item in FASE0):
            return (FASE0.index(item) +1) / 10

    return 0

def montagem(lista: list):
    resposta = []
    for item in lista:
        if(item != lista[1]):
            resposta.append(choice(item))
        else:
            resposta.append(item)
    
    return ' '.join(resposta)

def arvore(nota: float, conteudo: str, livro = ''):
    global sinalizadorLivro, sinalizadorCapitulo, sinalizadorVersiculo

    indice = int((notaExtra(conteudo))*10)
    resposta = choice(RefErro)
    #personagem que mais aparece
    if((nota >= 22 and nota < 28) and sinalizadorPersonagem == 1):
        if(indice == 0):
            resposta = montagem([RefPersonagem,RefQuantidadePos[0],RefFrequencia,RefResposta])
        else:
            resposta = montagem([RefInicio,str(indice)+"°", FASE2[:2], RefQuantidadePos[1:], RefFrequencia[5:],RefResposta])
        resposta += f" {maisCitado(indice)}"
            
    #personagem que menos aparece
    elif(nota >= 14 and nota < 18):
        if(indice == 0):
            resposta = montagem([RefPersonagem,RefQuantidadeNeg[0],RefFrequencia,RefResposta])
        else:
            resposta = montagem([RefInicio,str(indice)+"°", FASE2[:2], RefQuantidadeNeg[1:], RefFrequencia[5:],RefResposta])
        resposta += f" {menosCitado(indice)}"
            
    #maior livro
    elif(nota >= 18 and nota < 22):
        resposta = montagem([RefLivro, RefQuantidadePos[1], RefLivroConteudo,RefResposta])
        resposta += f" {maisCapitulo(indice)}"

    elif(nota >= 12 and nota < 14):
        resposta = montagem([RefLivro, RefQuantidadeNeg[1], RefLivroConteudo,RefResposta])
        resposta += f" {menosCapitulo(indice)}"
    
    #quantos livros, capitulos ou versiculos
    elif(nota >= 34 and nota < 38):

        if(qnNota(conteudo) == 0): #expande a possibilidade de termos(a entrada passa a se referir a biblia)
            nota+=1

        match(nota):
            case 34:#livro / velho testamento
                resposta = f"O velho testamento possui {totalLivros()} livros"    
            case 35:#capitulos / velho testamento
                resposta = f"O velho testamento possui {totalCapitulos()} capitulos"
            case 36:#versiculos / velho testamento
                resposta = f"O velho testamento possui {totalVersiculos()} versiculos"
            case 37:#personas / velho testamento
                resposta = f"O velho testamento possui {totalPersonagem()} personagens"
    
    elif(nota >= 38 and nota < 45):
        if(sinalizadorVersiculo == 1 or sinalizadorLivro == 1 and sinalizadorCapitulo == 0):
            resposta = f"O livro de {livro} tem {totalVersiculosLivro(livro)} versiculos"
        elif(sinalizadorCapitulo == 1 and sinalizadorLivro == 1):
            resposta = f"O livro {livro} tem {totalCapitulosLivro(livro)} capitulos"



    print(resposta)
    print(nota)
    sinalizadorLivro = 0
    sinalizadorCapitulo = 0
    sinalizadorVersiculo = 0

def start(entrada: str):
    if(entrada[-1] == '?'):
        entrada = entrada[:-1]
    conteudo = entrada.split()
    primeira = prNota(conteudo)
    segunda = sgNota(conteudo)
    terceira = trNota(conteudo)
    quarta = qrNota(conteudo)
    quinta = qnNota(conteudo)
    sexta = sxNota(conteudo)
    extra = notaExtra(conteudo)
    nota = primeira + segunda + terceira + quarta + quinta + sexta[0] + extra
    
    print(notaExtra(conteudo))
                            #nome do livro caso exista
    arvore(nota, conteudo, sexta[1] if len(sexta) > 1 else "")
    

#bug com a nota extra