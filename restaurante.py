cardapio = {
    100: {"nome": "Cachorro-quente", "preco": 1.20},
    101: {"nome": "Bauru Simples", "preco": 1.30},
    102: {"nome": "Bauru com Ovo", "preco": 1.50},
    103: {"nome": "Hamburger", "preco": 1.20},
    104: {"nome": "ChesseBurger", "preco": 1.70},
    105: {"nome": "Suco", "preco": 2.20},
    106: {"nome": "Refrigerante", "preco": 1.00},
}

# Função para calcular o valor do lanche
def calcular_valor(codigo, quantidade):
    if codigo in cardapio:
        preco_unitario = cardapio[codigo]["preco"]
        valor_total = preco_unitario * quantidade
        return valor_total
    else:
        return None

# Entrada de dados
codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

# Calcula o valor a ser pago
valor_a_pagar = calcular_valor(codigo, quantidade)

# Exibe o resultado
if valor_a_pagar is not None:
    print(f"Total a pagar: R$ {valor_a_pagar:.2f}")
else:
    print("Código de produto inválido.")