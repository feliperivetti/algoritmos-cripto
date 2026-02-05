import os
from unittest.mock import patch

from src.config import Settings


class TestConfig:
    """Testes para a configuração via Pydantic."""

    def test_default_values(self):
        """Testa os valores padrão."""
        # Limpa variáveis de ambiente para garantir defaults
        with patch.dict(os.environ, {}, clear=True):
            settings = Settings()
            assert settings.APP_NAME == "Algoritmos Cripto"
            assert settings.TIMEOUT_SECONDS == 20
            assert settings.LOG_LEVEL == "INFO"

    def test_env_var_override(self):
        """Testa sobrescrita por variáveis de ambiente."""
        with patch.dict(os.environ, {"APP_TIMEOUT_SECONDS": "60", "APP_LOG_LEVEL": "DEBUG"}):
            settings = Settings()
            assert settings.TIMEOUT_SECONDS == 60
            assert settings.LOG_LEVEL == "DEBUG"
