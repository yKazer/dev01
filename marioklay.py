def main():
    tamanho = int(input("Coloque um tamanho: "))
    if tamanho > 0:
        print("O tamanho é:","-" * tamanho)
    elif tamanho <= 0:
        print("Não existe tamanho negativo ou 0")
main()