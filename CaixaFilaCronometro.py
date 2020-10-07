#Simulador que retorna o tempo médio que clientes esperam na fila para usar o caixa eletrônico
#Trabalho feito por Felipe Scherer
#RA- D88HJE-1

from random import randint

def simula():
    expedienteDoBanco = calculaExpediente() * 60 *60 #Medido em segundos
    caixasEletronicos = calculaCaixasEletronicos()
    tempoDecorrido = 0
    totalClientes = 0
    totalTempoNaFila = 0
    filaClientes = []
    f = open("relatorio.txt", "w")
    while(True):
        #Para diminuir a quantidade de vezes que o programa roda, foi decidido que o programa irá rodar de 10 em 10 segundos

        print('-'*60)
        print(f'\033[35mMomento {tempoDecorrido}s\033[m')
        f.write("\n")
        f.write(f'Momento {tempoDecorrido}s\n') #Escreve no relatorio.txt 
        if(tempoDecorrido <= expedienteDoBanco):
            if(randint(1,5) > 1): #Aleatoriza a quantidade de cliente
                print(f"Cliente entrou no banco no tempo {tempoDecorrido}")
                f.write(f"Cliente entrou no banco no tempo {tempoDecorrido}\n")
                filaClientes.append(tempoDecorrido)
                totalClientes += 1

        for i in range(len(caixasEletronicos)):
            if(caixasEletronicos[i] == 0):
                print(f"Caixa {i} está livre")
                f.write(f"Caixa {i} esta livre\n")
                if (len(filaClientes) != 0): #Fila não está vazia
                    print(f"Cliente que chegou no horario {filaClientes[0]} está indo ao caixa {i}")
                    f.write(f"Cliente que chegou no horario {filaClientes[0]} esta indo ao caixa {i}\n")
                    totalTempoNaFila += tempoDecorrido - filaClientes[0]
                    filaClientes.pop(0)
                    caixasEletronicos[i] = escolheOperacao(f)
            else:
                caixasEletronicos[i] -= 10

        tempoDecorrido += 10
        if((tempoDecorrido >= expedienteDoBanco) and (len(filaClientes) == 0)):
            break
        
    f.close

    print(f"A quantidade de clientes que foram ao banco nessa simulação foi {totalClientes}")
    print(f"A média de espera na fila foi de {totalTempoNaFila/totalClientes}")

def escolheOperacao(f):
    operacao = randint(0,4)
    if(operacao == 0):
        #Saldo +10 s
        print(f'Cliente escolheu ver seu saldo que levou 10 segundos')
        f.write('Cliente escolheu ver seu saldo que levou 10 segundos\n')
        return 10
    elif(operacao == 1):
        #Saque +20 s
        print(f'Cliente escolheu fazer um saque que levou 20 segundos')
        f.write('Cliente escolheu fazer um saque que levou 20 segundos\n')
        return 20
    elif(operacao == 2):
        #Aplicação + 30s
        print(f'Cliente escolheu fazer uma aplicação que levou 30 segundos')
        f.write('Cliente escolheu fazer uma aplicacao que levou 30 segundos\n')
        return 30
    elif(operacao == 3):
        #Extrato Semanal +40 s
        print(f'Cliente escolheu fazer um extrato semanal que levou 40 segundos')
        f.write('Cliente escolheu fazer um extrato semanal que levou 40 segundos\n')
        return 40
    elif(operacao == 4):
        #Extrato Mensal + 50s
        print(f'Cliente escolheu fazer um extrato mensal que levou 50 segundos')
        f.write('Cliente escolheu fazer um extrato mensal que levou 50 segundos\n')
        return 50

def calculaCaixasEletronicos():
    x = ""
    while(True):
        try: 
            x = int(input(f"\033[33mQual a quantidade de caixas eletrônicos no banco? \033[m"))
            if x <= 0 or x >= 10:
                raise Exception()
            break
        except:
            print("\033[31mIsso não é um número válido")
            print("Escreva um número inteiro de \033[1;31m0 a 10\033[m")
    lista = []
    for i in range(x):
        lista.append(0)
    print(lista)
    return lista    

def calculaMediaClientes():
    x = ""
    while(True):
        try: 
            x = int(input(f"\033[33mQual a média de clientes que vão ao banco a cada 10 segundos? \033[m"))
            if x <= 0 or x > 10:
                raise Exception()
            break
        except:
            print("\033[31mIsso não é um número válido")
            print("Escreva um número inteiro de \033[1;31m1 a 10\033[m")
    return x

def calculaExpediente(): 
    x = ""
    while(True):
        try: 
            x = int(input(f"\033[33mPor quantas horas o banco fica aberto? \033[m"))
            if x <= 0 or x > 6:
                raise Exception()
            break
        except:
            print("\033[31mIsso não é um número válido")
            print("Escreva um número inteiro de \033[1;31m1 a 6\033[m")
            print("[31mMais que 6 horas pode travar sua IDE\033[m")
    return x


simula()

