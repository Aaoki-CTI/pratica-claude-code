import math


def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    """Divide a por b. Lança ValueError se b for zero."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b


def raiz_quadrada(n: float) -> float:
    """Calcula a raiz quadrada de um número real não-negativo."""
    if n < 0:
        raise ValueError("Raiz quadrada de número negativo não é definida nos reais")
    return math.sqrt(n)
