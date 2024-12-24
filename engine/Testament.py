import pandas as pd
import json
#lembrar da energia


class Testament():
    def __init__(self):
        self.dataFrame = pd.read_json("./engine/nvi.json", encoding="utf-8-sig")
        self.capitulos = self.dataFrame['chapters'][:39]

    def texto(self,livro=1, cap = 1, vers = 1):
        capitulosTotal = [item for item in self.capitulos[livro-1]]
        capitulo = [item for item in capitulosTotal[cap-1]]
        versiculo = capitulo[vers-1]
        return versiculo

        

obj = Testament()

print(obj.texto(5,2,3))