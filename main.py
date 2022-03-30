import Ldsec 

lista = Ldsec.Ldsec()


lista.inserirInicio('3')
lista.inserirInicio('2')
lista.inserirInicio('1')
lista.imprimir()
lista.inserirFim('4')
lista.inserirFim('5')

print('Primeiro elemento da lista: ', lista.getFirstElement())
print('Ultimo elemento da lista: ', lista.getLastElement())
print('Quantidade de elementos da lista: ', lista.getQuant())
print('Removendo o primeiro elemento: ', lista.removerInicio())
lista.imprimir()
print('Removendo o ultimo elemento: ', lista.removerFim())
lista.imprimir()
print("Contando todos os pares: ", lista.contarPares())
print("Consultando elemento 3 na lista: ", lista.consultarElemento(3))
lista.imprimir()
