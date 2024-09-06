# questao2.py

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n or n == 0

numero = int(input("Digite um número para verificar na sequência de Fibonacci: "))
if fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
