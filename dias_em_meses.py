#pedindo innformação
import os

def voltar_ao_menu():
    input('\nDigite qualquer tecla, para voltar ao menu\n')
    main()


def opcao_invalida():
    print('Está opção é invalida\n')
    voltar_ao_menu()


def opcão_principal():
    print("escolha um numero \n ")
    
    
def exibir_opcoes():
    print("28\n")
    print("30\n")
    print("31")

    
    
def coverter_opcao():
    try:
        opcao_escolhida= int(input())
        if opcao_escolhida == 28:
            print(f"O mês que tem {opcao_escolhida} Dias, é o mês 2")
        elif opcao_escolhida == 30:
            print(f'Os meses que tem {opcao_escolhida} Dias, são os meses 04, 06, 09, 11 ')
        elif opcao_escolhida == 31:
            print(f'Os meses que tem {opcao_escolhida} Dias, são os meses 01, 03, 05, 07, 08, 10, 12 ')
        else:
            print(f'O numero de dias {opcao_escolhida}, não corresponde a nenhum mês')
        voltar_ao_menu()
    except:
        opcao_invalida()
        

       

    
    
    
    
    
    
def main():
    os.system('cls')
    opcão_principal()
    exibir_opcoes()
    coverter_opcao()
    
    
    
if __name__ == '__main__':
    main()
        