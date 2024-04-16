#pedir numero pro usuario
letra = input("Digite uma Letra: \n").lower()

#execussão 

if letra in 'aeiou':
    print(f'A letra {letra}, é uma Vogal\n')
elif letra.isalpha():
    print(f'a letra {letra}, é uma consoante\n')
else:
    print('Essa letra não existe')