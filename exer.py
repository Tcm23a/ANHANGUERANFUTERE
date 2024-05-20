##Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

for i in range(1,6):
    print(i)

##Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
numerosReais= []

for i in range(11):
    numerosReais.append(float(i))
    
numerosReais.reverse()

print(numerosReais)

#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notasAlunos= []
quantidadeNotas= 0
numeroDaNota= 1


while quantidadeNotas <4:
    notasAlunos.append(int((input('Digite sua nota: '))))
    quantidadeNotas = quantidadeNotas +1
    
mediaAlunos = int(sum(notasAlunos)//4)

for notas in notasAlunos:
    print(f'A sua nota, {numeroDaNota} é: {notas}\n')
    numeroDaNota = numeroDaNota +1
    if numeroDaNota >4:
        print(f'A média das suas {quantidadeNotas} notas é igual a : {mediaAlunos}') 

##Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vogais_digitadas= []
consoantes_digitadas= []
quantidade_de_letras = 0
quantade_consoantes= 0
numero_da_consoante= 1

while quantidade_de_letras <11:
    letraDigita= (str(input('Digite uma letra:')))
    if letraDigita in 'aeiou':
        vogais_digitadas.append(letraDigita)
    else:
        consoantes_digitadas.append(letraDigita)
        quantade_consoantes= quantade_consoantes+1
            
    quantidade_de_letras = quantidade_de_letras+1

for consoantes in consoantes_digitadas:
    print(f'{numero_da_consoante} : {consoantes}')
    numero_da_consoante = numero_da_consoante +1
    
print(F'\nA quantidade de consoantes é : {quantade_consoantes}')    

##Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
numerosTodos= []
numerosImpares= []
numerosPares = []
quantidadeNumeros= 1

while quantidadeNumeros <= 20:
    numeros= int(input(f'\nDigite o {quantidadeNumeros}° : '))
    numerosTodos.append(numeros)
    if numeros %2 == 0:
        numerosPares.append(numeros)
    else:
        numerosImpares.append(numeros)
    quantidadeNumeros = quantidadeNumeros+1
    
print('Esses são todos os numeros digitados\n')    
    
for numbT in numerosTodos:
    
    print(f'{numbT}..')
    
print('Esses são os numeros Impares\n')

for numbI in numerosImpares:
    print(f'{numbI}')

print('Esses são os numeros pares: \n')

for numbP in numerosPares:
    print(f'{numbP}')

##faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

alunos = 10
notasAlunos= 4
numeroDaNota= 1
numerosDeMédia7= 0

medias= []

for aluno in range(alunos):
    for nota in range(notasAlunos):
        mediaDoAluno= int(input(f'Digite a sua {numeroDaNota}º :'))
        numeroDaNota= numeroDaNota+1
        
    mediaDoAluno=  mediaDoAluno/4
    medias.append(mediaDoAluno)
    numeroDaNota= numeroDaNota-4 
    
    if mediaDoAluno >=7:
        numerosDeMédia7 = numerosDeMédia7+1
        if numerosDeMédia7 >= 2:
            plu= 'alunos'
        else:
            plu= 'aluno'
    
print(f'O numero de alunos com a nota maior que 7 foram de {numerosDeMédia7} {plu}')



##Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
from functools import reduce

numeros = [1, 2, 3, 4, 5]

multiplicados = reduce((lambda x, y: x * y), numeros)

print("\nSoma: ", sum(numeros), "\nMultiplicão: ", multiplicados, "\nNúmeros: ", numeros)

##Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []
n_pessoa = 1

for i in range (5):
    print(f'digite a idade da {n_pessoa}º:  ')
    idadeUser = int(input('Digite a idade: '))
    alturaUser = int(input('Digite a altura: '))
    idade.append(idadeUser)
    altura.append(alturaUser)
    n_pessoa += 1

idade.reverse()
altura.reverse()
print(f'a idade é de{idade}, e a altura de {altura}')
