from engine.Arvore import Classificador

if __name__ == "__main__":
    tree = Classificador()
    while(True):
        init = str(input(">> "))
        
        if(init == '-e'):
            exit()
        
        if(len(init) > 1):
            tree.start(init)