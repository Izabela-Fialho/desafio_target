# Calcula o valor da primeira questao do desafio
from num2words import num2words

def q1(indice, k, soma):
    while(k < indice):
        k += 1
        soma += k
    return soma


def q2(num):
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

def q4(a):
    s_carro = 0
    s_caminhao = 100
    vel_carro = 110
    vel_caminhao = 80
    tempo_parada = 10
    tempo_sem_parada = s_caminhao/vel_caminhao
    tempo_com_parada = (tempo_parada/60) + tempo_sem_parada
    vel_caminhao = s_caminhao/tempo_com_parada
    tempo_encontro = (s_caminhao - s_carro)/(vel_carro + vel_caminhao)
    encontro = vel_carro * tempo_encontro
    print(f'O carro e caminhão se cruzarão a uma distância de {round(encontro,2)}km de Ribeirão Preto')