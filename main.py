import Ldsec 

lista = Ldsec.Ldsec()

if not lista.estahVazia():
    lista.removerInicio()

lista.inserirInicio('C')
lista.inserirInicio('B')
lista.inserirInicio('A')
lista.imprimir()
lista.inserirFim('D')
lista.inserirFim('E')

print('Primeiro elemento da lista: ', lista.getFirstElement())
print('Ultimo elemento da lista: ', lista.getLastElement())
print('Quantidade de elementos da lista: ', lista.getQuant())
print('Removendo o primeiro elemento: ')
print('Removendo o ultimo elemento: ')
lista.imprimir()

lista.removerInicio()
lista.imprimir()
lista.removerFim()
lista.imprimir()





'''
1) Sobre Listas Dinâmicas Simplesmente Encadeadas, implementar os seguintes métodos: 
inserir elemento em uma determinada posição na lista - inserirPosicao(valor, posicao)
remover elemento em uma determinada posição na lista - removerPosicao(posicao)
remover todas as ocorrências de um determinado elemento na lista - removerTodas(valor)
inserir um elemento após determinado elemento - inserirApos(valor1, valor2)  PS: valor1 = 

elemento a ser pesquisado na lista e valor2 = o elemento a ser inserido após valor1 
somar todos os elementos da lista - somarElementos() - PS: considerar que os elementos da lista sejam números
2) Sobre Listas Dinâmicas Simplesmente Encadeadas Circulares, implementar os seguintes métodos: 
trocar um elemento em uma determinada posição na lista por outro elemento - trocar(posicao, novovalor)
consultar o elemento anterior a um determinado elemento na lista - consultarAnterior(valor)
contar quantidade de elementos pares na lista - contarPares()
'''