"""
Testes para a Equação Diofantina.
"""

import pytest

from src.models.diofantina import DiofantinaModel


class TestDiofantinaModel:
    """Testes para DiofantinaModel."""

    @pytest.mark.parametrize(
        "a, b, c",
        [
            # Casos Básicos com Solução
            (3, 4, 7),
            (35, 15, 5),
            (10, 20, 30),
            # Casos com Zeros (se permitido pela lógica)
            # Nota: validate_non_zero proíbe 0, então 0 levanta erro na validação de input,
            # mas aqui testamos a lógica se o input passar ou testamos a validação separada.
            # O modelo atual usa validate_non_zero no get_params, mas o __init__ aceita int.
            # Vamos assumir que a lógica matemática lida com 0 se passar pelo init.
            # Porém, 0x + 5y = 10 -> 5y=10 -> y=2. Diofantina padrão geralmente assume a,b != 0
            # para algoritmos baseados em Euclides.
            # Se EuclidesModel recebe 0, ele pode falhar ou retornar.
            # Vamos testar apenas casos não-zero para 'solução existe' por enquanto,
            # e tratar zeros como edge case.
            # Coeficientes Negativos
            (-3, 4, 7),
            (3, -4, 7),
            (-3, -4, -7),
        ],
    )
    def test_solucao_valida(self, a, b, c):
        """Testa equações que DEVEM ter solução."""
        model = DiofantinaModel(a, b, c)
        result = model.solve()

        assert (
            result.metadata["has_solution"] is True
        ), f"Deveria ter solução para {a}x + {b}y = {c}"

        x0 = result.metadata["x0"]
        y0 = result.metadata["y0"]

        # Validar a solução particular: a*x0 + b*y0 = c
        assert a * x0 + b * y0 == c, f"Solução particular incorreta: {a}*{x0} + {b}*{y0} != {c}"

    @pytest.mark.parametrize(
        "a, b, c",
        [
            (6, 9, 5),  # MDC(6,9)=3, e 3 não divide 5
            (4, 8, 3),  # MDC(4,8)=4, e 4 não divide 3
            (10, 10, 5),  # MDC=10, 5 não divide
        ],
    )
    def test_sem_solucao(self, a, b, c):
        """Testa equações que NÃO devem ter solução."""
        model = DiofantinaModel(a, b, c)
        result = model.solve()

        assert result.metadata["has_solution"] is False
        assert result.result is None

    def test_solucao_geral_coeficientes(self):
        """Testa se os coeficientes da solução geral (t) estão corretos."""
        # Solução geral: x = x0 + (b/d)t, y = y0 - (a/d)t
        a, b, c = 35, 15, 5
        model = DiofantinaModel(a, b, c)
        result = model.solve()

        mdc = result.metadata["mdc"]  # 5
        x_coef = result.metadata["x_coef"]
        y_coef = result.metadata["y_coef"]

        # x_coef deve ser b/mdc -> 15/5 = 3
        # y_coef deve ser a/mdc -> 35/5 = 7
        assert x_coef == b // mdc
        assert y_coef == a // mdc

    @pytest.mark.parametrize("a, b, c", [(3, 4, 0), (-3, -4, 0)])
    def test_solucao_zero_homogenea(self, a, b, c):
        """Testa equação homogênea (c=0). Solução trivial (0,0) deve ser válida."""
        model = DiofantinaModel(a, b, c)
        result = model.solve()

        assert result.metadata["has_solution"] is True
        x0 = result.metadata["x0"]
        y0 = result.metadata["y0"]
        assert a * x0 + b * y0 == 0
