numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0

try:
    for numero in numeros:
        soma += numero

    
    print("A soma dos números é:", soma)

except Exception as erro:
    print("Ocorreu um erro:", erro)