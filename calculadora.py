"""Módulo com operações matemáticas básicas."""
import math


def somar(a: float, b: float) -> float:
    """Retorna a soma de a e b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Argumentos devem ser números")
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a subtração de b em a."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Argumentos devem ser números")
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de a e b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Argumentos devem ser números")
    return a * b


def dividir(a: float, b: float) -> float:
    """Divide a por b. Lança ValueError se b for zero."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Argumentos devem ser números")
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b


def raiz_quadrada(n: float) -> float:
    """Calcula a raiz quadrada de um número real não-negativo."""
    if not isinstance(n, (int, float)):
        raise TypeError("Argumentos devem ser números")
    if n < 0:
        raise ValueError("Raiz quadrada de número negativo não é definida nos reais")
    return math.sqrt(n)
