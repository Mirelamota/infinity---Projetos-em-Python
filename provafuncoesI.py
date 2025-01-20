#Desenvolva um programa em Python que funcione como uma calculadora simples, 
# permitindo ao usuário realizar as seguintes operações matemáticas:

#Soma
#Subtração
#Multiplicação
#Divisão
#Sair do programa
#Requisitos:
#O programa deve exibir um menu de opções, permitindo ao usuário escolher qual operação ele deseja realizar 
#(soma, subtração, multiplicação, divisão ou sair).
#Para cada operação escolhida, o programa deve solicitar ao usuário dois números 
#e exibir o resultado da operação entre eles.
#As operações matemáticas (soma, subtração, multiplicação e divisão) 
#devem ser implementadas em funções separadas. Cada função deve receber dois argumentos (números) 
#e retornar o resultado da operação.
#O programa deve funcionar indefinidamente, permitindo ao usuário realizar quantas operações quiser, 
#até que ele escolha a opção de sair.
#Caso o usuário selecione a divisão, o programa deve garantir que a divisão por zero seja evitada, 
#exibindo uma mensagem de erro apropriada e solicitando novos valores.
#Use condicionais e laços de repetição para controlar o fluxo do programa 
#e garantir que ele continue até o usuário escolher a opção de sair.

#Calculadora Simples

#Criando Funcões de Operações Matematicas

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Erro: Não é possivel dividir um número por zero.")
        return None
    return a / b

#criando uma Função para o Menu

def menu():
    print("\nCalculadora Simples")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    
def main():
    print("Iniciando a calculadora...")
    while True:
        menu()
        opcao = input("Escolha a opção (1 a 5): ")
        
        if opcao == "5":
            print("Saindo do Calculadora...")
            break
        
        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input('Digite o primeiro numero: '))
                num2 = float(input('Digite o segundo número: '))
            except ValueError:
                print("Por Favor, adicione numeros válidos.")
                continue
            
            if opcao == "1":
                print(f"Resultado: {somar(num1, num2)} ")
            elif opcao == "2":
                print(f'Resultado: {subtrair(num1, num2)}')
            elif opcao == '3':
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcao == "4":
                resultado = dividir(num1, num2)
                if resultado is not None:
                    print(f"Resultado: {resultado}")
            else:
                print("Não foi possível realizar a divisão.")

        else:
            print("Opção Invalida. Por favor, escolha uma opção correta.")
            
if __name__ == "__main__": 
    main()   
    

            

