
from desafio_target.module import q1,q2 ,q3 ,q4
 
print('\n')
print('Questão 1')
print(f'O Valor ao final do processamento é de: {q1(13,0,0)}')
print('\n')

print('\n')
print('Questão 2')
q2(int(input('Digite um valor para verificar se pertence a sequência de fibonacci: ')))
print('\n')

print('\n')
print('Questão 3')
q3(input('Escolha uma das sequências para descobrir seu próximo elemento: a) 1, 3, 5, 7, __ | b) 2, 4, 8 ,16 ,32 ,64, __ | c) 0, 1, 4, 9, 16, 25, 36, __ | d) 4, 16, 36, 64, __ | e) 1, 1, 2, 3, 5, 8, __ | f) 2, 10, 12, 16, 17, 18, 19, __ :'))
print('\n')

print('\n')
print('Questão 4')
q4('rb')
print('\n')

stringEntrada = input("5) Digite um texto para que tenha os cracteres invertidos: ")

stringInvertida = ""
for i in range(len(stringEntrada) - 1, -1, -1):
    stringInvertida += stringEntrada[i]

print('Seu texto invertido: {0}'.format(stringInvertida))

     