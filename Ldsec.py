class No:
    def __init__(self, info, proximo):
        self.info = info
        self.prox = proximo


class Ldsec:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def estaVazia(self):
        return self.quant == 0

    def getQuant(self):
        return self.quant

    def getFirstElement(self):
        if not self.estaVazia():
            return self.prim.info

    def getLastElement(self):
        if not self.estaVazia():
            return self.ult.info

    def inserirInicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.prim.prox = self.prim
        else:
            self.prim = No(valor, self.prim)
            self.ult.prox = self.prim
        self.quant += 1

    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.prim.prox = self.prim
        else:
            self.ult.prox = self.ult = No(valor, self.prim)
        self.quant += 1

    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.ult.prox = self.prim
        self.quant -= 1

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            aux.prox = self.prim
            self.ult = aux
        self.quant -= 1

    def imprimir(self):
        aux = self.prim
        i = 0
        while i < self.quant:
            print(aux.info, end=' ')
            aux = aux.prox
            i += 1
        print()
    
    def contarPares(self):
        aux  = self.prim
        par = 0;
        while self.ult.prox != self.prim:
            aux.info = aux 
            aux = self.ult
            if self.info % 2 == 0:
                par += 1;
        return par

    def consultarElemento(self, valor):
        aux = self.prim
        if self.quant == 1:
            aux.prox = self.ult
            if self.quant == valor:
                aux = aux.prox = self.prim
                print("Elemento existente ", valor)
            else:
                while aux.prox != self.prim:
                  aux = aux.prox
                  aux.prox.info = self.ult
            print(valor)
            
