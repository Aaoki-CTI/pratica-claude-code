import pytest
from calculadora import somar, subtrair, multiplicar, dividir, raiz_quadrada


# --- somar ---

def test_somar_inteiros():
    assert somar(2, 3) == 5


def test_somar_negativos():
    assert somar(-1, -4) == -5


def test_somar_float():
    assert somar(1.5, 2.5) == pytest.approx(4.0)


# --- subtrair ---

def test_subtrair_inteiros():
    assert subtrair(10, 4) == 6


def test_subtrair_resulta_negativo():
    assert subtrair(3, 7) == -4


# --- multiplicar ---

def test_multiplicar_inteiros():
    assert multiplicar(3, 4) == 12


def test_multiplicar_por_zero():
    assert multiplicar(99, 0) == 0


def test_multiplicar_negativos():
    assert multiplicar(-2, 5) == -10


# --- dividir ---

def test_dividir_inteiros():
    assert dividir(10, 2) == pytest.approx(5.0)


def test_dividir_resulta_float():
    assert dividir(7, 2) == pytest.approx(3.5)


def test_dividir_por_zero_lanca_excecao():
    with pytest.raises(ValueError, match="Divisão por zero não é permitida"):
        dividir(5, 0)


# --- raiz_quadrada ---

def test_raiz_quadrada_numero_positivo():
    assert raiz_quadrada(9) == pytest.approx(3.0)


def test_raiz_quadrada_zero():
    assert raiz_quadrada(0) == pytest.approx(0.0)


def test_raiz_quadrada_numero_decimal():
    assert raiz_quadrada(2) == pytest.approx(1.4142135623730951)


def test_raiz_quadrada_numero_grande():
    assert raiz_quadrada(1e10) == pytest.approx(1e5)


def test_raiz_quadrada_numero_pequeno():
    assert raiz_quadrada(1e-10) == pytest.approx(1e-5)


def test_raiz_quadrada_numero_negativo_lanca_excecao():
    with pytest.raises(ValueError, match="Raiz quadrada de número negativo não é definida nos reais"):
        raiz_quadrada(-4)
