import random #Biblioteca que permite números aleatórios
from datetime import datetime as dt
import datetime

def simulador():
    var_expediente = 5 #Expediente medido em horas
    var_media_cliente = def_retorna_media_cliente(var_expediente) #
    list_caixa_eletronico = ['11:00:00', '11:00:00', '11:00:00'] #def_retorna_quantidade_caixa_eletronico() #Guardaremos os caixas em uma lista que terá os valores 1(caixa sendo usado) ou 0(caixa livre)
    var_numero_cliente = 0 #Guarda o número do cliente atual
    list_clientes = [] #Lista que guarda os clientes com seus horários de chegada
    list_cliente_fila = [] #Fila do banco 


    for i in range(var_media_cliente): #Roda o for na quantidade de horas que o banco fica aberto
        if(random.randint(1,2) == 1):
            list_clientes.append(def_gera_tempo_chegada())
            #def_retorna_tempo_operacao_aleatoria()
            
    list_clientes = sorted(list_clientes) #Organiza a lista de tempos de chegada dos clientes
    print("-"*80)
    print(f"{len(list_clientes)} clientes foram ao banco nessa simulação com {len(list_caixa_eletronico)} caixas eletrônicos")
    


    print(list_clientes)
    formato_tempo = '%H:%M:%S'
    time_zero = dt.strptime('00:00:00', formato_tempo)
    for i in range(len(list_clientes)): #For da verdade
        tem_caixa_livre = False
        indice_caixa = 0
        for j in range(len(list_caixa_eletronico)):
            t1 = dt.strptime(list_caixa_eletronico[j], formato_tempo)
            t2 = dt.strptime(list_clientes[i], formato_tempo)
            print(t2-t1)
            if ((t2 - t1).time() >= time_zero.time()) : #Achou caixa livre
                tem_caixa_livre = True
                indice_caixa = j

        if(tem_caixa_livre): #Achou caixa livre, aqui iremos fazer a operação
            print(f'O caixa {indice_caixa} está vazio e será usado pelo cliente {i + 1} que chegou {list_clientes[i]}')
            list_caixa_eletronico[indice_caixa] = 1
        else:
            print(f'Todos os caixas estão ocupados, o cliente {i + 1} está esperando na fila')

        
   
    tempo_inicial = '11:00:00'
    tempo_final = '16:00:00'

    
    t1 =  dt.strptime(list_clientes[1], formato_tempo)
    t2 = dt.strptime('00:00:40', formato_tempo)
    
    tdelta = (t1- time_zero + t2).time()
    #tdelta = datetime.timedelta(hours=11, minutes=0, seconds=0) + datetime.timedelta(seconds=40)

    print(tdelta)

def def_gera_tempo_chegada():
    # generate random number scaled to number of seconds in a day
    # (6*60*60) = 18000
    
    tempo_random = int(random.random()*18000) #random.random() gera um float 0.alguma coisa
    
    horas   = int(tempo_random/3600)
    minutos = int((tempo_random - horas*3600)/60)
    segundos = tempo_random - horas*3600 - minutos*60
    
    tempo_final = '%02d:%02d:%02d' % (horas + 11, minutos, segundos) #Somamos 11 as horas, porque o banco abre as 11
    return tempo_final

def def_retorna_media_cliente(var_expediente): #Retorna a média de clientes que entram no banco a cada minuto
    x = ""
    while(True):
        try: 
            x = int(input(f"\033[33mQual a média de clientes por dia ({var_expediente} horas) no banco? \033[m"))
            if x <= 0: #or x > 100:
                raise Exception()
            break
        except:
            print("\033[31mIsso não é um número válido")
            print("Escreva um número inteiro de \033[1;31m0 a 50\033[m")
    return x

def def_retorna_quantidade_caixa_eletronico(): #Pede a quantidade de caixas eletronicos que existe nessa simulação
    x = ""
    while(True):
        try: 
            x = int(input(f"\033[33mQual a quantidade de caixas eletrônicos no banco? \033[m"))
            if x <= 0 or x > 10:
                raise Exception()
            break
        except:
            print("\033[31mIsso não é um número válido")
            print("Escreva um número inteiro de \033[1;31m0 a 10\033[m")
    lista = []
    for i in range(x):
        lista.append(0)
    return lista

def def_retorna_tempo_operacao_aleatoria(): #Retorna o tempo gasto de uma operação aletória do caixa eletrônico
    var_operacao = random.randint(0,4)
    if(var_operacao == 0):
        #Operação escolhida igual a Saldo, com o tempo de 10 segundos
        print("Operação Saldo, com o tempo de 10 segundos")
        return 10
    elif(var_operacao == 1):
        #Operação escolhida igual a Saque, com o tempo de 20 segundos
        print("Operação Saque, com o tempo de 20 segundos")
        return 20
    elif(var_operacao == 2):
        #Operação escolhida igual a Aplicação, com o tempo de 30 segundos
        print("Operação Aplicação, com o tempo de 30 segundos")
        return 30
    elif(var_operacao == 3):
        #Operação escolhida igual a Extrato Semanal, com o tempo de 40 segundos
        print("Operação Extrato Semanal, com o tempo de 40 segundos")
        return 40
    elif(var_operacao == 4):
        #Operação escolhida igual a Extrato Mensal, com o tempo de 50 segundos
        print("Operação Extrato Mensal, com o tempo de 50 segundos")
        return 50

simulador()


'''
def def_organiza_lista(lista): #Organiza a lista de números passada
    def busca_menor(lista,indice): #Indice valor que deverá ser contado para ser ordenado
        menor_valor = int(lista[0][indice-1:indice+1])
        menor_indice = 0
        for i in range(1,len(lista)):
            if int(lista[i][indice-1:indice+1]) < menor_valor: #segundo número das horas
                menor_valor = int(lista[i][indice-1:indice+1])
                menor_indice = i
        return menor_indice
            
    lista_ordenada = []
    
    for i in range(len(lista)):
        menor = busca_menor(lista, 1)
        lista_ordenada.append(lista.pop(menor))
        

    for i in range(len(lista)):
        if lista[i-1][0:2] == lista[i][0:2]:
            print(lista[i-1][0:2])
            print(lista[i][0:2])
            menor = busca_menor(lista, 4)
            lista_ordenada.append(lista.pop(menor))

    for i in range(len(lista)):
        print("oi")
        menor = busca_menor(lista, 7)
        lista_ordenada.append(lista.pop(menor))       
        
    return lista_ordenada'''

'''
list_aux_minutos = [] 
        for i in range(var_media_cliente): #Roda o for quantas vezes for a média de clientes por hora    
            if(random.randint(1,2) == 1): #Verificação para deixar o programa mais aleatório ainda, com margem de erro
                tempo_chegada_minutos = random.randint(1,60)
                list_aux_minutos.append(tempo_chegada_minutos)
            var_numero_cliente += 1             
        list_aux_minutos = def_organiza_lista(list_aux_minutos)
        list_aux_2 = []
        for j in list_aux_minutos:
            var_segundo_random = random.randint(1,60)
            list_aux_2.append([hora, j])

        list_clientes.append(list_aux_2)'''