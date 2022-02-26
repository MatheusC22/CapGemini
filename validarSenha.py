import re
'''verificar: função que verifica se os requisitos da
senha são atendidos e retorna quantos caracteres sao necessarios
no minimo para satizfaze-los'''
def verificar(senha:str) ->int:
    minuscula = False  #
    maiuscula = False  # Auxiliares para verificar se os requisitos foram atendidas 
    num = False        # 
    especial = False   #
    
    falta = 0

    if re.search("[A-Z]",senha):            #
        maiuscula = True                    #
    if re.search("[a-z]",senha):            # Utiliza Regex para identificar caracteres na String:senha
        minuscula = True                    # e muda o valor das auxiliares pra True
    if re.search("[1-9]",senha):            #
        num = True                          #
    if re.search("[!@#$%^&*()+-]",senha):   #
        especial = True

    if maiuscula and minuscula and num and especial == True: # Verifica se todos os requisitos foram atendidos 
        if len(senha) < 6:  # Verifica se a senha tem ao menos 6 caracteres
            falta = 6 - len(senha)
            return falta
    else:
        if maiuscula == False:  #
            falta+=1            #
        if minuscula == False:  #
            falta+=1            # Adciona mais um ao minimo de caracteres necessarios para cada 
        if especial == False:   # requisito não comprido
            falta+=1            #
        if num == False:        #
            falta+=1
        if len(senha) < 6:
            if falta > 6 - len(senha): # Verfica se o minimo de caracteres necessarios é maior que 6(minimo da senha)
                return falta
            else:
                return 6 - len(senha)

senha = input()
print(verificar(senha))