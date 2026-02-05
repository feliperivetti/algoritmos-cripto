from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configurações centralizadas da aplicação.

    Os valores podem ser sobrescritos por variáveis de ambiente.
    Exemplo: APP_TIMEOUT=60
    """
    APP_NAME: str = "Algoritmos Cripto"
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"
    TIMEOUT_SECONDS: int = 20

    class Config:
        env_prefix = "APP_"


settings = Settings()
