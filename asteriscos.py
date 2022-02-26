#author: matheus Colombo

#build: função que controi escada de *
def build(tam:int):
    espaco = " "#espaco: auxiliar para adcionar espaços
    linha = ""#linha: auxiliar utilizada pra printar as linhas no loop

    for i in range(tam+1): #define altura da escada de *
        for j in range (tam):#define a largura de escada de *
            if j < tam-i:
                linha += espaco# preenche os espacos vazios com " " 
            else:
                linha += "*"# preenche o restante com *
        
        print(linha)
        linha = "" #reseta a auxiliar para o proximo loop
tamanho = int(input())
build(tamanho)
    