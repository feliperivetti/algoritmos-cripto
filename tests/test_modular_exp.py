"""
Testes para a Exponenciação Modular.
"""

import pytest

from src.models.modular_exp import ModularExpModel


class TestModularExpModel:
    """Testes para ModularExpModel."""

    @pytest.mark.parametrize("a, b, n, expected_result", [
        # Casos Básicos
        (2, 4, 5, 1),   # 2^4 = 16 = 1 mod 5
        (3, 4, 7, 4),   # 3^4 = 81 = 4 mod 7
        (5, 3, 13, 8),  # 5^3 = 125 = 8 mod 13

        # Casos onde o ciclo é importante (b grande)
        # 2^10 mod 5. Ciclo de 2 mod 5 é [2, 4, 3, 1] (tam 4). 10 % 4 = 2. Elemento índice 2 é 4.
        # Espera: 1024 % 5 = 4.
        (2, 10, 5, 4),

        # Edge Cases
        (10, 5, 1, 0),  # Mod 1 é sempre 0
        (1, 100, 5, 1), # 1^b = 1
        (5, 1, 10, 5),  # a^1 = a
        (7, 0, 5, 1),   # a^0 = 1
    ])
    def test_calculo_modular(self, a, b, n, expected_result):
        """Testa o cálculo final de a^b mod n."""
        if n == 0:
            return  # Evita erro em teste mal parametrizado (não deve ocorrer aqui)

        model = ModularExpModel(a, b, n)
        result = model.solve()

        assert result.result == expected_result
        assert result.metadata["a"] == a
        assert result.metadata["n"] == n

    def test_cycle_detection_metadata(self):
        """Verifica se os metadados do ciclo estão corretos para um caso conhecido."""
        # 2 mod 5: Ciclo [2, 4, 3, 1] -> Tam 4
        model = ModularExpModel(2, 10, 5)
        result = model.solve()

        assert result.metadata["cycle_length"] == 4
        remainders = result.metadata["remainders"]
        assert remainders[1] == 2
        assert remainders[2] == 4
        assert remainders[3] == 3
        assert remainders[4] == 1

    def test_large_exponent_optimization(self):
        """
        Testa se o algoritmo usa o ciclo para calcular expoente grande
        sem iterar b vezes.
        """
        # 2 mod 5 tem ciclo 4.
        # 2^1000003 mod 5.
        # 1000003 % 4 = 3.
        # Resultado deve ser o 3º do ciclo -> 3.

        a, b, n = 2, 1000003, 5
        model = ModularExpModel(a, b, n)
        result = model.solve()

        assert result.result == 3
        # O número de passos registrados deve ser pequeno (tamanho do ciclo), e não 1 milhão
        assert len(result.steps) <= 10  # Ciclo de 2 mod 5 é 4
