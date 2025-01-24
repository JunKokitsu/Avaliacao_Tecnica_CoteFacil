def fibonacci(n, memo=None):
 
    #Calcula o enésimo número da sequência de fibonacci de forma otimizada usando recursao e vetor
    #:param n: Posicao na sequencia (n >= 0)
    #:param memo: Lista para armazenar os resultados intermediarios (usada para memorizacao)
    #:return: Enesimo numero da sequencia de Fibonacci

    if n < 0:
        raise ValueError("O valor de n deve ser maior ou igual a 0")

    # Inicializa o vetor de memorização na primeira chamada
    if memo is None:
        memo = [None] * (n + 1)

    # Caso base
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Se o resultado foi calculado, retorna do vetor
    if memo[n] is not None:
        return memo[n]

    # Caso contrario, calcula e armazena no vetor
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Exemplo de uso
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python fibonacci2.py n")
    else:
        try:
            n = int(sys.argv[1])
            print(f"{n}-esimo numero da sequencia de Fibonacci: {fibonacci(n)}")
        except ValueError:
            print("Por favor, entre com um numero inteiro maior ou igual a 0")