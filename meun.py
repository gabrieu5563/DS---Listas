import os
os.system("cls")

while True:
    os.system("cls")

    print("1 - Exiba o primeiro elemento do vetor ")
    print("2 - Exiba somente os numeros negativos")
    print("3 - Exiba a soma dos valores do vetor")
    print("4 - Exiba a media dos elementos do vetor")
    print("5 - Exiba os numeros impares presentes no vetor")
    volta = int(input("Digite o exercicio: "))
    match volta:
        case 1:
            import ex1
            ex1
            os.system("pause")

        case 2:
            import ex2
            ex2
            os.system("pause")

        case 3:
            import ex3
            ex3
            os.system("pause")

        case 4:
            import ex4
            ex4
            os.system("pause")

        case 5:
            import ex5
            ex5
            os.system("pause")

        case 0:
            break

        case _:
            print("Digite uma opção válida.")
            os.system("pause")