#Variáveis de caixa guardam quanto tempo o caixa está em uso, 0 está livre
#Variaveis de cliente guardam quanto tempo ele está esperando na fila

expediente = 8 #Medido em horas

caixa1 = 0
caixa2 = 0
caixa3 = 0



def simula(qnt_cliente_hora, expediente):
    for i in range(expediente):
        for i in range(qnt_cliente_hora):
            print("Cliente")
        print("Rodou uma vez")



def init():
    media_clientes_por_hora = ""  #Variável que guarda a quantidade de clientes por hora
    while(True):
        try: 
            media_clientes_por_hora = int(input("Qual a média de clientes por hora no banco? "))
            if media_clientes_por_hora <= 0 or media_clientes_por_hora > 50:
                raise Exception()
            break 
        except:
            print("Isso não é um número válido")
    return media_clientes_por_hora


simula(init(), expediente)
