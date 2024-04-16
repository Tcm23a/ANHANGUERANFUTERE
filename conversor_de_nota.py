def converter_nota(nota):
    if nota >=  86:
        return 'A NOTA É A'
    elif nota >= 61:
        return 'A NOTA É B'
    elif nota >= 36:
        return ' A NOTA É C'
    elif nota >= 1:
        return 'A NOTA É D'
    else:
        return 'A NOTA É E'
    

nota= float(input("Qual foi sua nota ?"))
conceito = converter_nota(nota)
print(f"O conceito correnponde a nota {nota} é {conceito}.")