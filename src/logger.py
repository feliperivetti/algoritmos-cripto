import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging(log_level: int = logging.INFO) -> None:
    """
    Configura o sistema de logging da aplicação.

    Cria uma pasta 'logs/' se não existir e define dois handlers:
    1. RotatingFileHandler: Grava em 'logs/app.log' (max 5MB, 3 backups)
    2. StreamHandler: Grava no console (stdout)
    """
    # Cria diretório de logs se necessário
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, "app.log")

    # Formato do log
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
    )

    # Handler para Arquivo (Rotativo)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Handler para Console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Configuração Raiz
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    # Evita duplicidade de handlers se a função for chamada mais de uma vez
    if not root_logger.handlers:
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)

    logging.info("Sistema de logging inicializado.")
