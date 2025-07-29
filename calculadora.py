# 🧮 Calculadora Simples em Python
# Autor: Myrelle Torres
# Descrição: Calculadora com operações básicas (soma, subtração, multiplicação e divisão)

def soma(x, y):
    return x + y

def subtrai(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    return x / y

print("\n🧮 Calculadora Simples\n")
print("Escolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# Entrada do usuário
opcao = input("Digite a opção (1/2/3/4): ")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        resultado = soma(num1, num2)
        operacao = '+'
    elif opcao == '2':
        resultado = subtrai(num1, num2)
        operacao = '-'
    elif opcao == '3':
        resultado = multiplica(num1, num2)
        operacao = '*'
    elif opcao == '4':
        resultado = divide(num1, num2)
        operacao = '/'
    else:
        resultado = "Opção inválida!"
        operacao = ''

    if operacao:
        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
    else:
        print(f"\n{resultado}")

except ValueError:
    print("\nErro: por favor, insira apenas números válidos.")
