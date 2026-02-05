import pytest

from src.models.teorema_chines import TeoremaChinesModel


class TestTeoremaChines:
    """Testes para o Teorema Chinês do Resto."""

    def test_sun_tzu_problem(self):
        """
        O problema clássico de Sun Tzu:
        x ≡ 2 (mod 3)
        x ≡ 3 (mod 5)
        x ≡ 2 (mod 7)
        Solução: 23
        """
        # Entrada simulada como string (vinda da UI)
        model = TeoremaChinesModel(a_list="2, 3, 2", m_list="3, 5, 7")
        result = model.solve()
        
        assert result.result == 23
        assert result.metadata["M"] == 105  # 3*5*7

    def test_single_equation(self):
        """Testa caso trivial com 1 equação."""
        # x ≡ 3 (mod 10) -> x = 3
        model = TeoremaChinesModel(a_list="3", m_list="10")
        result = model.solve()
        
        assert result.result == 3

    def test_non_coprime_moduli_error(self):
        """Testa se detecta módulos não coprimos."""
        # m1=2, m2=4 (gcd=2)
        model = TeoremaChinesModel(a_list="1, 1", m_list="2, 4")
        result = model.solve()
        
        assert result.metadata["error"] is True
        assert "gcd(2, 4) != 1" in result.metadata["error_message"]

    def test_mismatched_input_length(self):
        """Testa listas de tamanhos diferentes."""
        model = TeoremaChinesModel(a_list="1, 2", m_list="3")
        result = model.solve()
        
        assert result.metadata["error"] is True
        assert "tamanho" in result.metadata["error_message"].lower()

    def test_invalid_input_format(self):
        """Testa input inválido (não numérico)."""
        model = TeoremaChinesModel(a_list="a, b", m_list="3, 5")
        # Deve ter listas vazias devido ao try-catch no init
        assert model.a_values == []
        
        # Deve retornar erro de entrada vazia ou inválida, dependendo de como o solve trata lista vazia
        result = model.solve()
        assert result.metadata["error"] is True
