def reverse_string(s):
    # Inicializa uma nova string para armazenar o resultado
    result = ""
    # Percorre a string de entrada de trás para frente
    for character in s[::-1]:
        # Concatena cada caractere na nova string
        result += character
    return result

# Substitua 'YourStringHere' com a string que você deseja inverter
input_string = 'Estágio Ribeirão Preto - 2024'
reversed_string = reverse_string(input_string)
print("String invertida:", reversed_string)