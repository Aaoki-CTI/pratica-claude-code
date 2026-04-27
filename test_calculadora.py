import pytest
from calculadora import soma, subtracao, multiplicacao, divisao


class TestSoma:
    def test_soma_inteiros(self):
        assert soma(2, 3) == 5

    def test_soma_negativos(self):
        assert soma(-1, -4) == -5

    def test_soma_floats(self):
        assert soma(1.5, 2.5) == 4.0

    def test_soma_tipo_invalido(self):
        with pytest.raises(TypeError):
            soma("2", 3)


class TestSubtracao:
    def test_subtracao_inteiros(self):
        assert subtracao(10, 4) == 6

    def test_subtracao_negativos(self):
        assert subtracao(-5, -3) == -2

    def test_subtracao_floats(self):
        assert subtracao(5.5, 2.5) == 3.0

    def test_subtracao_tipo_invalido(self):
        with pytest.raises(TypeError):
            subtracao("a", 1)


class TestMultiplicacao:
    def test_multiplicacao_inteiros(self):
        assert multiplicacao(3, 4) == 12

    def test_multiplicacao_por_zero(self):
        assert multiplicacao(99, 0) == 0

    def test_multiplicacao_negativos(self):
        assert multiplicacao(-2, 5) == -10

    def test_multiplicacao_tipo_invalido(self):
        with pytest.raises(TypeError):
            multiplicacao(None, 2)


class TestDivisao:
    def test_divisao_inteiros(self):
        assert divisao(10, 2) == 5.0

    def test_divisao_floats(self):
        assert divisao(7.5, 2.5) == 3.0

    def test_divisao_negativos(self):
        assert divisao(-9, 3) == -3.0

    def test_divisao_por_zero(self):
        with pytest.raises(ValueError, match="Divisão por zero não é permitida"):
            divisao(10, 0)

    def test_divisao_tipo_invalido(self):
        with pytest.raises(TypeError):
            divisao("10", 2)
