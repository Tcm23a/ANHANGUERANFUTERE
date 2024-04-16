#Pedindo Numero
import os

def exibir_titulo():
    print("""
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░  ███████╗███╗░░░███╗
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝████╗░████║
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║  █████╗░░██╔████╔██║
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║  ██╔══╝░░██║╚██╔╝██║
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║  ███████╗██║░╚═╝░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚══════╝╚═╝░░░░░╚═╝

██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝""")
    
def voltar_ao_menu():
    input('Digite qualquer tecla para voltar ao menu principal:\n')
    main()

def mensagem_de_erro():
    print('\nEsse sinal não exite....')
    voltar_ao_menu()
    
def escolher_numeros():
    try:
        numero_1= int(input('\n Digite o Primeiro Numero: \n '))
        numero_2= int(input('\n Digite o segundo Numero: \n'))
        print(f'\nOs numeros escolhidos foram {numero_1} | {numero_2}\n')
        print('\n Digite 1 para + ')
        print('\n Digite 2 para - ') 
        print('\n Digite 3 para % ') 
        print('\n Digite 4 para X ')
        sinal = int(input())
        if sinal == 1:
            calculo= int(numero_1+numero_2)
            sinal= 'Mais'
        elif sinal == 2:
            calculo= int(numero_1-numero_2)
            sinal= 'Menos'
        elif sinal == 3:
            calculo= int(numero_1/numero_2)
            sinal= 'Dividido'
        elif sinal == 4:
            calculo= int(numero_1*numero_2)
            sinal= 'Vezes'
        print (f'\nO resultado de {numero_1}, {sinal}, {numero_2}, é igual a {calculo}.....')
            
            
        voltar_ao_menu()
    except:
        mensagem_de_erro()
            






















def main():
    os.system('cls')
    exibir_titulo()
    escolher_numeros()
    
    
    
if __name__ == '__main__':
    main()