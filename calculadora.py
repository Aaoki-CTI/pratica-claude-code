"""Módulo com operações matemáticas básicas."""


def soma(a: float, b: float) -> float:
    """Retorna a soma de a e b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Argumentos devem ser números")
    return a + b


def subtracao(a: float, b: float) -> float:
    """Retorna a subtração de b em a."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Argumentos devem ser números")
    return a - b


def multiplicacao(a: float, b: float) -> float:
    """Retorna o produto de a e b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Argumentos devem ser números")
    return a * b


def divisao(a: float, b: float) -> float:
    """Retorna a divisão de a por b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Argumentos devem ser números")
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b
