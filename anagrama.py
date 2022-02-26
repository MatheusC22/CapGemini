import re
def reverseString(text):# ReverseString:função que inverte uma dada string
    return ''.join(reversed(text))

def verificar(palavra:str) ->int : # Verificar: função que verifica quantos anagrams há em uma palavra
    pares = int()
    tamanho = len(palavra)-1
    whitelistA=[]   #
    whitelistB=[]   # Auxiliares para armazenas o index dos caracteres
    lista = []      #

    for i in range(len(palavra)):                          #
        for j in range(i+1,len(palavra)):                  # Pega os caracteres duplicados e coloca-os em uma array
            if palavra[i] == palavra[j]:                   #
                whitelistA.append(palavra.find(palavra[i]))#

    reversa = reverseString(palavra)# inverte a palavra para buscar pelos pares dos caracteres

    for i in range(len(palavra)):                          #
        for j in range(i+1,len(palavra)):                  # Pega os caracteres duplicados da palavra invertida e coloca-os em um array
            if reversa[i] == reversa[j]:                   #
                whitelistB.append(reversa.find(reversa[i]))#

    whitelistB = list(reversed(whitelistB))

    for i in range(len(whitelistA)):         #
        lista.append(whitelistA[i])          # juntas as duas listas dos pares
        lista.append(tamanho - whitelistB[i])#

    pares = len(lista)/2 # faz o calculo de quantos pares simples tem na palavra. ex(qq,ii,aa)

    for i in range(0,len(lista),2):  #
        if lista[i+1] - lista[i] > 1:# procura por anagramas com mais de 2 letras
            pares += 1               #
    
    return round(pares)
x = input()
print(verificar(x))
