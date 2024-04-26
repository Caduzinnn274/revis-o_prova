valores = [10, 20, 30, 40, 50]

try:
    media = sum(valores) / len(valores)
    print("A média dos valores é:", media)

except ZeroDivisionError:
    print("A lista está vazia. Não é possível calcular a média.")

except Exception as e:
    print("Ocorreu um erro:", e)