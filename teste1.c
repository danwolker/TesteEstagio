#include <stdio.h>

int main() {
    // Declaração e inicialização de variáveis
    int INDICE = 13, SOMA = 0, K = 0;

    // Loop que continua enquanto K for menor que INDICE
    while (K < INDICE) {
        K = K + 1; // Incrementa K por 1
        SOMA = SOMA + K; // Adiciona o valor atual de K à soma total
    }

    // Imprime o valor final da soma
    printf("O valor final da variável SOMA é: %d\n", SOMA);

    return 0; // Indica que o programa foi concluído com sucesso
}

// Ao final do processamento, o valor da variável SOMA será 91. //