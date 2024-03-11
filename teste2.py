def is_fibonacci(num):
    # Define os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Verifica se o número é um dos dois primeiros números da sequência de Fibonacci
    if num == a or num == b:
        return True
    
    # Calcula os próximos números da sequência até que seja maior ou igual ao número informado
    while b < num:
        a, b = b, a + b  # Atualiza os valores para os próximos dois números da sequência
    
    # Verifica se o número está na sequência de Fibonacci
    return num == b

# Solicita ao usuário que digite um número para verificar se está na sequência de Fibonacci
numero = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))

# Verifica se o número pertence à sequência de Fibonacci
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
