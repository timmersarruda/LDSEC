# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:23:26 2022

@author: PC
"""

class No:
    def __init__(self, info, proximo):
        self.info = info
        self.prox = proximo
        

class Ldsec:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def estahVazia(self):
        return self.quant == 0
    
    def getQuant(self):
        return self.quant 
    
    def getFistElement(self):
        if not self.estahVazia():
            return self.prim.info
        
    def getLastElement(self):
        if not self.estahVazia():
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
        if self.quant == 0 :
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, self.prim)
        self.quant += 1    
        
    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.ult.prox
            self.prim.prox = self.prim
        self.quant -= 1
        
    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim 
            while aux.prox != self.ult:
                aux = aux.prox 
                aux.prox = self.prim 
            aux.prox = self.prim
            self.ult = aux 
        self.quant -= 1 
                   
    def imprimir(self):
        aux = self.prim
        while aux.prox != self.ult:
            print(aux.info, end=' ')
            aux = aux.prox
            print() 