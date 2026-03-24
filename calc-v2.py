def decimal_para_binario(n):
    return bin(n)[2:]

def binario_para_decimal(b):
    return int(b, 2)

def decimal_para_octal(n):
    return oct(n)[2:]

def octal_para_decimal(o):
    return int(o, 8)

def decimal_para_hex(n):
    return hex(n)[2:].upper()

def hex_para_decimal(h):
    return int(h, 16)

def hex_para_binario(h):
    return bin(int(h, 16))[2:]

def hex_para_octal(h):
    return oct(int(h, 16))[2:]


def menu():
    print("\n===== CALCULADORA DE BASES =====")
    print("1 - Decimal → Binário")
    print("2 - Binário → Decimal")
    print("3 - Decimal → Octal")
    print("4 - Octal → Decimal")
    print("5 - Decimal → Hexadecimal")
    print("6 - Hexadecimal → Decimal")
    print("7 - Hexadecimal → Binário")
    print("8 - Hexadecimal → Octal")
    print("0 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                n = int(input("Digite um número decimal: "))
                print("Resultado:", decimal_para_binario(n))

            elif opcao == "2":
                b = input("Digite um número binário: ")
                print("Resultado:", binario_para_decimal(b))

            elif opcao == "3":
                n = int(input("Digite um número decimal: "))
                print("Resultado:", decimal_para_octal(n))

            elif opcao == "4":
                o = input("Digite um número octal: ")
                print("Resultado:", octal_para_decimal(o))

            elif opcao == "5":
                n = int(input("Digite um número decimal: "))
                print("Resultado:", decimal_para_hex(n))

            elif opcao == "6":
                h = input("Digite um número hexadecimal: ")
                print("Resultado:", hex_para_decimal(h))

            elif opcao == "7":
                h = input("Digite um número hexadecimal: ")
                print("Resultado:", hex_para_binario(h))

            elif opcao == "8":
                h = input("Digite um número hexadecimal: ")
                print("Resultado:", hex_para_octal(h))

            elif opcao == "0":
                print("Encerrando...")
                break

            else:
                print("Opção inválida!")

        except ValueError:
            print("Erro: entrada inválida! Tente novamente.")


if __name__ == "__main__":
    main()