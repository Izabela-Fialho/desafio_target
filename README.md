# Desafio Target Sistemas
Nesse repositório você encontrará as soluções do desafio proposto no recrutamento.
Linguagem utilizada: Python.

## Requirements
```sh
$ pip install num2words
```
## Questões
Questão 1:
Observe o trecho de código abaixo:

    int INDICE = 13, SOMA = 0, K = 0;

    enquanto K < INDICE faça
    {
    	K = K + 1;
    	SOMA = SOMA + K;
    }

    imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

### Solução: Ao final do processamento o valor será 91

Questão 2:
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

### Solução: def q2(num):
    n1 = 0
    n2 = 1
    n3 = 0
    list_fibo = [n1, n2]
    while(n3 < num):
        n3 = n1+n2
        n1 = n2
        n2 = n3
        list_fibo.append(n3)
    print(f'Sequência gerada: f{list_fibo}')
    if n3 == num:
        print(f'O número {num} pertence a da sequência de fibonacci, sendo a soma de: {list_fibo[len(list_fibo)-2]} + {list_fibo[len(list_fibo)-3]}')
    else:
        print(f'O número: {num} não esta incluso na sequência de fibonacci')
    

Questão 3:
Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, __ 
b) 2, 4, 8 ,16 32 , 64, __ 
c) 0, 1, 4, 9, 16, 25, 36, __
d) 4, 16, 36, 64, __
e) 1, 1, 2, 3, 5, 8, __
f) 2, 10, 12, 16, 17, 18, 19, __

### Solução:
    def q3(alternativa):    
        if alternativa == 'a' or alternativa == 'A':
            lista = [1,3,5,7]
            lista.append('x')
            print(f'O próximo elemento será: {2 * lista.index("x") +1}')
        elif alternativa == 'b' or alternativa == 'B':
            lista = [2,4,8,16,32,64]
            lista.append('x')
            print(f'O próximo elemento será: {2**(lista.index("x")+1)}')
        elif alternativa == 'c' or alternativa == 'C':
            lista = [0,1,4,9,16,25,36]
            lista.append('x')
            print(f'O próximo elemento será: {lista.index("x")**2}')
        elif alternativa == 'd' or alternativa == 'D':
            lista = [4,16,36,64]
            lista.append('x')
            print(f'O próximo elemento será: {(2*(lista.index("x")+1))**2}')
        elif alternativa == 'e' or alternativa == 'E':
            lista = [1,1,2,3,5,8]
            lista.append('x')
            print(f'O próximo elemento será: {(lista.index("x") - 1) + (lista.index("x") + 2)}')
        elif alternativa == 'f' or alternativa == 'F':
            lista = [2,10,12,16,17,18,19]
            lista.append(lista[len(lista)-1]+1)
            while(num2words(lista[len(lista)-1], lang='pt-br')[0] != 'd'):
                lista.append(lista[len(lista)-1]+1)
            print(f'O próximo elemento será: {lista[len(lista)-1]}')

Questão 4:
Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Riberão Preto em direção a Franca, a uma velocidade constante de 110km/h e o caminhão de Franca em direção a Riberão Preto a uma velocidade constante de 80km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Riberão Petro?


Questão 5:
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

### Solução:
    stringEntrada = input("5) Digite um texto para que tenha os cracteres invertidos: ")

    stringInvertida = ""
    for i in range(len(stringEntrada) - 1, -1, -1):
        stringInvertida += stringEntrada[i]

    print('Seu texto invertido: {0}'.format(stringInvertida))



