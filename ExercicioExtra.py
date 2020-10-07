'''Um sistema de impressão concorrente

'''

from string import ascii_uppercase
import random

def geraStringAleatoria():
    tamanhoDaString = random.randint(1,10)
    letrasPossiveis = ascii_uppercase
    return ''.join(random.choice(letrasPossiveis) for i in range(tamanhoDaString))


impressoras = []
arquivos = []
numeroImpressoras = int(input('Qual a quantidade de impressoras que estão conectadas? '))
for i in range(numeroImpressoras):
    impressoras.append('')
qntArquivosASeremImpressos = int(input('Qual a quantidade de arquivos que deverão ser impressos? '))
for i in range(qntArquivosASeremImpressos):
    arquivos.append(geraStringAleatoria())

arquivos = sorted(arquivos, key=len, reverse=True)


print(f"Estado impressoras: {impressoras}")
print(f"Estado arquivos: {arquivos}")

while(len(arquivos) > 0):
    for i in range(len(impressoras)):
        if(impressoras[i] == ''):
            if(len(arquivos) > len(impressoras)):
                print(len(arquivos))
                if(arquivos[i] == ''):
                    arquivos.pop(i)
                else:
                    impressoras[i] = arquivos[i][0]
                    arquivos[i] = arquivos[i][1:]
            
                #Sobrou arquivos que devem ser impressos na mesma impressora
            else:
                for k in arquivos:
                    if(k != ''):
                        for j in range(len(impressoras)):
                            if(impressoras[j] == ''):
                                impressoras[j] = arquivos[i][0]
                                arquivos[j] = arquivos[j][1:]

    print('-'*50)
    print(f"Estado impressoras: {impressoras}")
    print(f"Estado arquivos: {arquivos}")
    for i in range(len(impressoras)):
        impressoras[i] = ''
    apagaArquivos = True
    for i in arquivos:
        if(i != ''):
            apagaArquivos = False
    if(apagaArquivos):
        for i in range(0, len(arquivos)): 
            arquivos.pop() 