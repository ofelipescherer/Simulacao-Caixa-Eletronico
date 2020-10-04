import random #Biblioteca que permite números aleatórios

def simulador():
    var_media_cliente = def_retorna_media_cliente_hora() #
    var_expediente = 8 #Expediente medido em horas
    var_numero_cliente = 0 #Guarda o número do cliente atual
    list_clientes = [] #Lista que guarda os clientes com seus horários de chegada
    list_cliente_fila = [] #Fila do banco 
    var_is_caixa1_free = True #True significa está livre
    var_is_caixa2_free = True
    var_is_caixa3_free = True

    for hora in range(var_expediente): #Roda o for na quantidade de horas que o banco fica aberto
        list_aux = [] 
        for i in range(var_media_cliente): #Roda o for quantas vezes for a média de clientes por hora    
            if(random.randint(1,2) == 1): #Verificação para deixar o programa mais aleatório ainda, com margem de erro
                tempo_chegada = random.randint(1,60)
                list_aux.append(tempo_chegada)
            var_numero_cliente += 1
        list_aux = def_organiza_lista(list_aux)
        list_aux_2 = []
        for j in list_aux:
            list_aux_2.append([hora, j])

        list_clientes.append(list_aux_2)
            

    print(list_clientes)

def def_retorna_media_cliente_hora(): #Retorna a média de clientes que entram no banco a cada hora
    x = ""
    while(True):
        try: 
            x = int(input("\033[33mQual a média de clientes por hora no banco? \033[m"))
            if x <= 0 or x > 50:
                raise Exception()
            break
        except:
            print("\033[31mIsso não é um número válido")
            print("Escreva um número inteiro de \033[1;31m0 a 50\033[m")
    return x

def def_organiza_lista(lista): #Organiza a lista de números passada
    def buscaMenor(array):
        menor_valor = array[0]
        menor_indice = 0

        for i in range(1, len(array)):
            if(array[i] < menor_valor):
                menor_valor = array[i]
                menor_indice = i
        return menor_indice

    lista_ordenado = []
    for i in range(len(lista)):
        menor = buscaMenor(lista)
        lista_ordenado.append(lista.pop(menor))
    return lista_ordenado


simulador()