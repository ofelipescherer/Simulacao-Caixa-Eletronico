# Simulacao-Caixa-Eletronico

Esse é um projeto feito para a aula de Estrutura de Dados na Unip

Projeto feito por Felipe Scherer

É simulado uma situação onde deve existir caixa eletrônicos e clientes (aleatórios) devem usar eles.
Caso tenha mais que 3 clientes (quantidade de caixas eletrônicos) os próximos deverão ser guardados em uma fila.
No final, o objetivo é calcular quanto tempo médio os clientes ficaram na fila

### Enunciado
Aplicação de Filas: Simulando a fila de um caixa eletrônico

Pretende-se simular uma situação que nos permita determinar qual o tempo médio que um
cliente aguarda numa fila, para realizar uma transação no caixa eletrônico de uma agencia
bancária.
O caixa eletrônico oferece cinco opções ao cliente e, através de estatísticas, chegamos ao tempo
médio necessário para realizar cada uma das transações possíveis:
| Transação | Código | Tempo (s) |
| ------ | ------ | ------ |
| Saldo | 0 | 10 |
| Saque | 1 | 20 |
| Aplicação | 2 | 30 | 
| Extrato Semanal | 3 | 40 |
| Extrato Mensal 4 | 50 |

Sabe-se que a agência tem três caixas eletrônicos que atendem a uma única fila de clientes. À
medida que qualquer um dos caixas fica livre, o primeiro cliente da fila o utiliza.
Quando um cliente entra na fila, o horário é anotado. Quando ele sai, verifica-se quanto tempo
ele aguardou e este valor é acumulado. Também o total de clientes é registrado, de modo que
no final do expediente, seja possível determinar o tempo médio que um cliente permanece na
fila para utilizar o caixa.
Duas entidades concretas estão envolvidas nesse problema: caixas e clientes. Vamos abstrair
destas entidades apenas os atributos essenciais para a resolução do problema, objetivando uma
implementação simples e funcional.
Tudo o que precisamos saber sobre um caixa é se ele está ocupado ou não. Caso esteja,
precisamos ter uma “noção” de por quanto tempo ele ainda será usado pelo cliente. Assim, cada
caixa será representado por uma variável inteira, cujo valor indica por quantos minutos ele
permanecerá ocupado. Se o valor dessa variável for 0, então o caixa está livre. Inicialmente,
todos os caixas estão livres. Quando um cliente inicia uma transação num caixa, o tempo
necessário para realizar a transação escolhido por ele é que determinará quanto tempo o caixa
permanecerá ocupado.
A outra entidade que precisamos representar é o cliente. Dele só nos interessa o momento em
que ele entrou na fila para que, ao sair, possamos calcular quanto tempo ele aguardou. Portanto,
cada cliente será representado por um número inteiro correspondente ao horário em que ele
entrou na fila.

Na nossa simulação, dois eventos que podem ocorrer são de interesse particular:
• Um cliente chega na agência e entra na fila;
• Um caixa é liberado, alguém sai da fila e o utiliza.
Para sincronizar estes eventos, vamos assumir que temos um cronômetro que marca unidade
de tempo. Durante uma unidade de tempo, que poderia ser um segundo, qualquer combinação
dos eventos pode ocorrer, até mesmo nenhuma.
Para simular a dinâmica com que os eventos ocorrem, procedemos como segue:
• Zerar o cronômetro
• Enquanto não terminar o expediente:
a) Se um cliente chegou, então entra na fila;
b) Se fila não está vazia e um caixa está livre, então cliente inicia transação;
c) Para cada caixa ocupado, decrementar o seu tempo de uso;
d) Incrementar o cronômetro.
Alguns pontos do algoritmo acima devem ser detalhados para que possamos programa-los:
Terminou o expediente?
Para determinar o final do expediente, usamos o próprio cronômetro. Para isto, basta definir o
período de atendimento da agência em termos das unidades de tempo marcadas pelo
cronômetro. Quando o cronômetro atingir o valor definido, então terminou o expediente.
Chegou um cliente?
Numa situação real, não teremos cliente chegando à agência a cada minuto para usar o caixa
eletrônico. Para implementar esta parte do algoritmo, de modo que tenhamos algo não
sistemático, podemos utilizar uma função que a cada chamada retorne um valor aleatório.
Cliente entra na fila.
Convencionamos representar um cliente apenas pelo horário em que ele entrou na fila. O tempo
está sendo controlado pelo cronômetro. Logo, colocar um cliente na fila equivale a
simplesmente armazenar nela o valor corrente do cronômetro, no momento que ele chega.
Inicia transação.
Quando um caixa é liberado e um cliente começa a utilizá-lo, precisamos saber por quanto
tempo ele estará ocupado. O tempo de uso do caixa depende da transação que é iniciada pelo
cliente. Aqui também é interessante que as transações iniciadas sejam aleatórias.

Bibliografia:
Pereira, S. L. Estruturas de dados fundamentais: conceitos e aplicações. São Paulo, Editora Érica.
8a edição, 2004.
