##Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

for i in range(1,6):
    print(i)

##Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
numerosReais= []

for i in range(11):
    numerosReais.append(float(i))
    
numerosReais.reverse()

print(numerosReais)

##Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

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
##faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
##Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
##Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.