from engine.Data import * 
from random import choice, choices

class Arvore:
    def __init__(self, name = ''):
        self.pontuacao = 0
        self.ord = 0
        self.tex = 0
        self.liv = 0
        self.cap = 0
        self.ver = 0
        self.per = 0
        self.sin = 0
        self.plu = 0
        self.qua = 0
        self.pos = 0
        self.med = 0
        self.neg = 0
        self.num = -1
        self.name = name

    def main(self):
        #menor quantidade
        if(self.neg == 1):
            if(self.pontuacao >= 4 and self.pontuacao <= 13):
                if(self.sin == 1):
                    if(self.per == 1): #personagem menos citado
                        pass
                    elif(self.ver == 1 and self.liv == 0):#menor versiculo
                        pass
                    elif(self.cap == 1 and self.liv == 0):#menor capitulo
                        pass
                    elif(self.liv == 1):#menor livro
                        pass

                elif(self.plu == 1):
                    if(self.per == 1): #personagens menos citados
                        pass
                    elif(self.ver == 1 and self.liv == 0): #menores versiculos
                        pass
                    elif(self.cap == 1 and self.liv == 0): #menores capitulos
                        pass
                    elif(self.liv == 1): #menores livros
                        pass
        
        #maior quantidade
        elif(self.pos == 1):
            if(self.pontuacao >= 8 and self.pontuacao <= 21):
                if(self.sin == 1):
                    if(self.per == 1): #personagem mais citado
                        pass
                    elif(self.ver == 1 and self.liv == 0): #maior versiculo
                        pass
                    elif(self.cap == 1 and self.liv == 0): #maior capitulo
                        pass
                    elif(self.liv == 1): #maior livro
                        pass
                elif(self.plu == 1):
                    if(self.per == 1): #personagens mais citados
                        pass
                    elif(self.ver == 1 and self.liv == 0): #maiores versiculos
                        pass
                    elif(self.cap == 1 and self.liv == 0): #maiores capitulos
                        pass
                    elif(self.liv == 1): #maiores livros
                        pass
            
            #medias
            elif(self.med == 1):
                if(self.pontuacao >= 12 and self.pontuacao <= 40):
                    if(self.per == 1):
                        if(self.liv == 1): #personagens por livro
                            pass

                        elif(self.cap == 1): #personagens por capitulo
                            pass

                        elif(self.ver == 1): #personagen por versiculo
                            pass

                    elif(self.ver == 1):
                        if(self.liv == 1): #versiculo por livro
                            pass

                        elif(self.cap == 1): #versiculo por capitulo
                            pass

                    elif(self.cap == 1 and self.liv == 1): #capitulos por livro
                        pass

            #quantidades
            elif(self.qua == 1):
                if(self.pontuacao >= 33 and self.pontuacao <= 86):
                    if(self.per == 1):
                        if(self.liv == 1): #personagens e um livro especifico
                            pass
                        
                        else: #personagens em toda biblia
                            pass

                    elif(self.ver == 1):
                        if(self.liv == 1):
                            if(self.cap == 1): #versiculos em um capitulo especifico
                                pass
                            
                            else: #versiculos em todo livro
                                pass
                        
                        else: #versiculos em toda biblia
                            pass
                    
                    elif(self.cap == 1):
                        if(self.liv == 1): #capitulos em um livro especifico
                            pass

                        else: #capitulos em toda biblia
                            pass
            
            #textos
            if(self.name != ''):
                if(self.cap == 1):
                    if(self.ver == 1): #versiculo especifico
                        pass
                    
                    else: #todo texto de um capitulo
                        pass
                
                else: #todo texto de um livro
                    pass
            
    

class Classificador:
    def __init__(self):
        self.entrada: str

        #Sinalizadores para auxiliar a classificação dos dados
        self.sinOrdinal = 0 #indica que a busca possui um termo ordinal (primeiro, segundo etc...)
        self.sinTexto = 0 #indica que a busca é para um texto
        self.sinLivro = 0 #indica que a busca é para um livro
        self.sinCapitulo = 0 #indica que a busca é para um capitulo
        self.sinVersiculo = 0 #indica que a busca é para um versiculo
        self.sinPersonagem = 0 #indica que a busca é para um personagem
        self.sinSingular = 0 #indica que a busca é para apenas um elemento
        self.sinQuant = 0 #indica que a busca é para uma quantidade
        self.sinPlural = 0 #indica que a busca é para mais de um elemento
        self.sinQuanPos = 0 #indica que a busca possui um quantificador positivo
        self.sinQuanMed = 0 #indica que a busca possui um qauntificador medio
        self.sinQuanNeg = 0 #indica que a busca possui um quantificador negativo
        self.sinNumero = [0] #sinalizador especial, ele deve ser usado para coletar um numero
        self.sinEscrita = [0,''] #sinaliza que a busca é para um conteudo da biblia

    #funções para definir os pontos da entrada
    def fPronome(self, arg: list):
        pronomes = ('qual','quem')
        pronomesPlural = ('quantos','quantas')
        pontos = 0
        for item in arg:
            if(item in pronomes):
                self.sinSingular = 1 #a busca é para um unico elemento
                if(item == 'quem'): #nota maior para o termo 'quem', indica que é um personagem
                    self.sinPersonagem = 1
                    pontos+= 3
            
                pontos += 1
            
            if(item in pronomesPlural):
                self.sinPlural = 1
                self.sinQuant = 1
                pontos+= 5

        return pontos
    
    def fSubistantivo(self, arg: list):
        substantivos = ('personagem','pessoa','individuo','livro','capitulo','versiculo')
        substantivosPlural = ('personagens','pessoas','individulos','livros','capitulos','versiculos')
        pontos = 0
        for item in arg:
            if(item in substantivos):
                self.sinSingular = 1
                if(item in substantivos[:3]): #indica que a busca é para um personagem
                    self.sinPersonagem = 1
                    pontos += 3
                if(item in substantivos[3:]): #indica que a busca é para um texto
                    self.sinTexto = 1
                
                    match(item):
                        case 'versiculo':self.sinVersiculo = 1
                        case 'capitulo':self.sinCapitulo = 1
                        case 'livro':self.sinLivro = 1

                    pontos += 3
            
            if(item in substantivosPlural):
                self.sinPlural = 1
                if(item in substantivosPlural[:3]): 
                    self.sinPersonagem = 1
                    pontos += 8
            if(item in substantivosPlural[3:]): 
                    self.sinTexto = 1
                    match(item):
                        case 'versiculos':self.sinVersiculo = 1
                        case 'capitulos':self.sinCapitulo = 1
                        case 'livros':self.sinLivro = 1
                        
                    pontos += 8
            
        return pontos
    
    def fQuantificador(self, arg: list):
        quantificadorPositivo = ('mais','maior','maiores')
        quantificadorMedio = ('media','meio')
        quantificadorNegativo = ('menos','menor','menores')
        pontos = 0
        for item in arg:
            if(item in quantificadorPositivo):
                self.sinQuanPos = 1
                pontos += 5
            if(item in quantificadorMedio):
                self.sinQuanMed = 1
                pontos += 3
            if(item in quantificadorNegativo):
                self.sinQuanNeg = 1
                pontos += 1
        return pontos
    
    def fVerbos(self, arg: list):
        verbos = (
            'aparece','apareceu','citado(a)','mencionado(a)','ocorreu',
            'tem','existe','existem','ha','aparecem','possui','escrito')
        pontos = 0
        for item in arg:
            if(item in verbos):
                if(item in verbos[:5]): #indicação de ocorrencia, aparição
                    pontos += 10
                if(item in verbos[5:]): #indicação de existencia, posseção
                    pontos += 20
                    if(item == 'escrito'):
                        self.sinEscrita[0] = 1
        return pontos
    
    def fLivros(self, arg: list):
        livros = [str(nome).lower() for nome in NOMES[:]]
        pontos = 0
        for item in arg:
            if(item in livros):
                self.sinLivro = 1
                pontos += 50
                self.sinEscrita[1] = item
            
        return pontos
    
    def fOrdinal(self, arg: list):
        ordinais = ('primeiro','segundo','terceiro','quarto','quinto','sexto','setimo','oitavo','nono')

        for item in arg:
            if(item in ordinais or str(item).isdigit()):
                self.sinOrdinal = 1
                self.sinSingular = 1

                if(item not in ordinais):
                    self.sinNumero.append(int(item)) 
                else:
                    self.sinNumero.append(ordinais.index(item)) 
    
    def limparSinal(self):
        self.sinOrdinal = 0
        self.sinTexto = 0
        self.sinLivro = 0
        self.sinCapitulo = 0
        self.sinVersiculo = 0
        self.sinPersonagem = 0
        self.sinQuant = 0
        self.sinQuanPos = 0
        self.sinQuanMed = 0
        self.sinQuanNeg = 0
        self.sinPlural = 0
        self.sinSingular = 0
        self.sinNumero = [0]
        self.sinEscrita = [0,'']

    def mostrarSinal(self):
        print(f"ordem:{self.sinOrdinal}")
        print(f"texto:{self.sinTexto}")
        print(f"Livro:{self.sinLivro}")
        print(f"Capitulo:{self.sinCapitulo}")
        print(f"Versiculo:{self.sinVersiculo}")
        print(f"Personagem:{self.sinPersonagem}")
        print(f"Quant:{self.sinQuant}")
        print(f"QuanPos:{self.sinQuanPos}")
        print(f"QuanMed:{self.sinQuanMed}")
        print(f"QuanNeg:{self.sinQuanNeg}")
        print(f"Plural:{self.sinPlural}")
        print(f"Singular:{self.sinSingular}")
        print(f"Numero:{self.sinNumero[:]}")
        print(f"Escrita: {self.sinEscrita[:]}")


    #não recebe parametros pois usa a entrada global
    def pontuacao(self):
        conteudo = self.entrada.split()

        pronome = self.fPronome(conteudo)
        substantivo = self.fSubistantivo(conteudo)
        quantificador = self.fQuantificador(conteudo)
        verbo = self.fVerbos(conteudo)
        livro = self.fLivros(conteudo)

        self.fOrdinal(conteudo)

        pontos = pronome + substantivo + quantificador + verbo + livro
        return pontos
    
    def iniciarArvore(self, pontos):
        arvore = Arvore(self.sinEscrita[1])
        arvore.pontuacao = pontos
        arvore.ord = self.sinOrdinal
        arvore.tex = self.sinTexto
        arvore.cap = self.sinCapitulo
        arvore.liv = self.sinLivro
        arvore.ver = self.sinVersiculo
        arvore.qua = self.sinQuant
        arvore.pos = self.sinQuanPos
        arvore.med = self.sinQuanMed
        arvore.neg = self.sinQuanNeg
        arvore.num = self.sinNumero[:]
        arvore.plu = self.sinPlural
        arvore.sin = self.sinSingular

        arvore.main()


    def start(self, entrada:str):
        if(entrada[-1] == "?"):
            entrada = entrada[:-1] #remove o '?'
        
        entrada = entrada.lower() #coloca todas as letras em minusculos
        self.entrada = entrada
        
        pontos = self.pontuacao()
        print(pontos)
        
        self.iniciarArvore(pontos)

        self.mostrarSinal()
        self.limparSinal()


