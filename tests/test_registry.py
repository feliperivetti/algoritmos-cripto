
import pytest

from src.exceptions import AlgorithmNotFoundError
from src.models.base import BaseAlgorithm
from src.registry import AlgorithmRegistry
from src.views.base_view import BaseView


class MockModel(BaseAlgorithm):
    def solve(self):
        pass

    @classmethod
    def get_params(cls):
        return {}


class MockView(BaseView):
    def render(self, result):
        pass


class TestAlgorithmRegistry:
    """Testes para o Registro de Algoritmos."""

    def test_register_and_get(self):
        """Testa o registro e recuperação de um algoritmo."""
        AlgorithmRegistry.register("mock_algo", MockModel, MockView)

        config = AlgorithmRegistry.get("mock_algo")
        assert config["model"] == MockModel
        assert config["view"] == MockView

    def test_get_non_existent(self):
        """Testa se lança exceção correta para algoritmo inexistente."""
        with pytest.raises(AlgorithmNotFoundError) as excinfo:
            AlgorithmRegistry.get("nao_existe")

        assert "Algoritmo não encontrado: nao_existe" in str(excinfo.value)
