# 🧮 Calculadora Simples em Python
# Autor: Myrelle Torres
# Descrição: Calculadora com operações básicas (soma, subtração, multiplicação e divisão)

# Função para somar dois números
def soma(x, y):  # recebe dois valores e retorna a soma
    return x + y

# Função para subtrair dois números
def subtrai(x, y):  # recebe dois valores e retorna a subtração
    return x - y

# Função para multiplicar dois números
def multiplica(x, y):  # recebe dois valores e retorna o produto
    return x * y

# Função para dividir dois números
def divide(x, y):  # recebe dois valores e retorna a divisão
    if y == 0:  # verifica se o divisor é zero
        return "Erro: divisão por zero!"  # mensagem de erro
    return x / y  # retorna o resultado da divisão

# Exibe o menu inicial
print("\n🧮 Calculadora Simples\n")  # título
print("Escolha a operação:")  # instrução para o usuário
print("1 - Soma (+)")          # opção 1
print("2 - Subtração (-)")     # opção 2
print("3 - Multiplicação (*)") # opção 3
print("4 - Divisão (/)")       # opção 4

# Entrada do usuário para escolher a operação
opcao = input("Digite a opção (1/2/3/4): ")  # lê a escolha do usuário

try:
    # Entrada dos números
    num1 = float(input("Digite o primeiro número: "))  # lê o primeiro número
    num2 = float(input("Digite o segundo número: "))   # lê o segundo número

    # Verifica a opção escolhida e executa a operação correspondente
    if opcao == '1':  # se a opção for 1
        resultado = soma(num1, num2)  # chama a função soma
        operacao = '+'  # guarda o símbolo da operação
    elif opcao == '2':  # se a opção for 2
        resultado = subtrai(num1, num2)  # chama a função subtrai
        operacao = '-'  # guarda o símbolo
    elif opcao == '3':  # se a opção for 3
        resultado = multiplica(num1, num2)  # chama a função multiplica
        operacao = '*'  # guarda o símbolo
    elif opcao == '4':  # se a opção for 4
        resultado = divide(num1, num2)  # chama a função divide
        operacao = '/'  # guarda o símbolo
    else:  # se não for nenhuma das opções
        resultado = "Opção inválida!"  # mensagem de erro
        operacao = ''  # vazio para não imprimir operação inválida

    # Exibe o resultado final
    if operacao:  # se houver uma operação válida
        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
    else:  # caso contrário
        print(f"\n{resultado}")

except ValueError:  # se o usuário digitar algo que não seja número
    print("\nErro: por favor, insira apenas números válidos.")
