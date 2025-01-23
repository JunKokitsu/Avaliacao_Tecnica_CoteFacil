import sys

def fibonacci(n):
    # Calcula o enésimo número da sequência de Fibonacci usando recursão.
    #:param n: Posição na sequência (n >= 0).
    #:return: Enésimo número da sequência de Fibonacci.
    
    if n < 0:
        raise ValueError("O valor de n deve ser maior ou igual a 0")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    #execute o programa com: python fibonacci.py n
    if len(sys.argv) != 2:
        print("Uso: python fibonacci.py n")
        print("Substitua n por um número inteiro maior ou igual a 0 para calcular o enésimo número da sequência de fibonacci")
    else:
        try:
            n = int(sys.argv[1])
            print(f"O {n}° número da sequência de fibonacci é: {fibonacci(n)}")
        except ValueError:
            print("Insira um número inteiro maior ou igual a 0")