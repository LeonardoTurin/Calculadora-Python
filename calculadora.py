import math

def calculadora():
    print("Bem-vindo à Calculadora Completa!")
    print("Operações disponíveis:")
    print("1: Adição")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("5: Potência")
    print("6: Raiz Quadrada")
    print("7: Porcentagem")
    print("8: Logaritmo")
    print("9: Seno")
    print("10: Cosseno")
    print("11: Tangente")

    operacao = input("Escolha a operação (1/2/3/4/5/6/7/8/9/10/11): ")

    if operacao in ['1', '2', '3', '4', '5', '7']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operacao == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operacao == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operacao == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Erro: Divisão por zero!")
        elif operacao == '5':
            print(f"{num1} ^ {num2} = {num1 ** num2}")
        elif operacao == '7':
            print(f"{num1}% de {num2} = {num1 * num2 / 100}")

    elif operacao in ['6', '8', '9', '10', '11']:
        num = float(input("Digite o número: "))

        if operacao == '6':
            if num >= 0:
                print(f"√{num} = {math.sqrt(num)}")
            else:
                print("Erro: Raiz quadrada de número negativo!")
        elif operacao == '8':
            if num > 0:
                print(f"log({num}) = {math.log10(num)}")
            else:
                print("Erro: Logaritmo de número não positivo!")
        elif operacao == '9':
            print(f"sen({num}) = {math.sin(math.radians(num))}")
        elif operacao == '10':
            print(f"cos({num}) = {math.cos(math.radians(num))}")
        elif operacao == '11':
            print(f"tan({num}) = {math.tan(math.radians(num))}")

    else:
        print("Operação inválida!")

    continuar = input("Deseja fazer outra operação? (s/n): ")
    if continuar.lower() == 's':
        calculadora()
    else:
        print("Obrigado por usar a calculadora!")

# Iniciar a calculadora
calculadora()