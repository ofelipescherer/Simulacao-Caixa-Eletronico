'''
Habilite 'toggle word warp'
Exercício Extra- Enunciado-
Sabemos que a velocidade de processamento de um computador é muito superior à velocidade de uma impressora. Geralmente, durante a impressão de um arquivo, a maior parte do tempo o computador fica aguardando a impressora terminar de imprimir uma parte dos dados para poder enviar outra.
Se a quantidade de arquivos que temos a imprimir é muito volumosa, então o computador é subutilizado, ficando ocioso a maior parte do tempo. Temos que encontrar uma forma de otimizar este processo, de modo a aproveitar melhor os recursos disponíveis.
Um microcomputador, do tipo IBM-PC, suporta até três impressoras paralelas que podem ser utilizadas ao mesmo tempo. Cada impressora é acessível através de uma das três portas portas paralelas que são denominadas Lpt1, Lpt2 e Lpt3. Suponha então uma situação onde temos um micro dedicado única e exclusivamente à impressão de um arquivo de texto e a ele estão conectadas três impressoras, uma em cada porta.
Desejamos um programa que gerencie o uso das impressoras concorrentemente. Por exemplo, imagine que temos para imprimir os arquivos A, B e C. Ao invés de imprimi-los um de cada vez, vamos imprimi-los simultaneamente, um em cada impressora do sistema. O micro envia uma parte do texto A para a primeira porta. Ao invés de ficar aguardando, envia uma parte do arquivo B para a segunda porta e uma parte do arquivo C para a terceira porta. neste momento, o micro volta à primeira impressora( que já terminou de imprimir a parte enviada) e pode então enviar uma segunda parte do arquivo... O processo se repete até que os três arquivos tenham sido inteiramente impressos.
Entretanto, admitindo que temos ainda outros arquivos para imprimir, não é viável esperar até que os três sejam completamente impressos para selecionar mais três. Imagine que os arquivos A e B tenham apenas 10kbytes cada, enquanto o arquivo C tem 350 kbytes, neste caso, teremos duas impressoras ociosas por muito tempo.
O ideal, portanto, é ocupar imediatamente uma impressora que terminou de imprimir um arquivo, selecionando-se outro para que ela imprima. Temos que tomar cuidado para que um arquivo não comece a ser impresso numa impressora e termine em outra.
Cada arquivo a ser impresso será representado pelo seu nome em disco, na forma de uma cadeia de caracteres. Uma fila pode ser utilizada para armazenar os arquivos que aguardam até serem selecionados para impressão e, para cada impressora, precisamos conhecer as seguintes informações:
-Está livre?
-Qual o nome do arquivo sendo impresso?
-Qual o estado corrente da impressão?
-Qual a porta paralela associada?

Feito por Felipe Scherer
RA-D88HJE-1

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
            if(arquivos[i] == ''):
                arquivos.pop(i)
            else:
                impressoras[i] = arquivos[i][0]
                arquivos[i] = arquivos[i][1:]

    print('-'*50)
    print(f"Estado impressoras: {impressoras}")
    print(f"Estado arquivos: {arquivos}")
    for i in range(len(impressoras)):
        impressoras[i] = ''
