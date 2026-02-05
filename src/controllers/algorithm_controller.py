import concurrent.futures
import logging
from typing import Type

import streamlit as st

from src.config import settings
from src.models.base import AlgorithmResult, BaseAlgorithm
from src.registry import AlgorithmRegistry
from src.validators.input_validators import InputValidator
from src.views.base_view import BaseView

logger = logging.getLogger(__name__)


@st.cache_data(show_spinner=False)
def _run_algorithm_cached(algorithm_name: str, params: dict) -> AlgorithmResult:
    """
    Executa o algoritmo com cache e limite de tempo.
    Se exceder settings.TIMEOUT_SECONDS, retorna um resultado de erro (que também é cacheado).
    """
    logger.info("Executando: %s com params=%s", algorithm_name, params)

    config = AlgorithmRegistry.get(algorithm_name)
    model_class = config["model"]
    model = model_class(**params)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(model.solve)
        try:
            result = future.result(timeout=settings.TIMEOUT_SECONDS)
            logger.info("Execução finalizada com sucesso: %s", algorithm_name)
            return result
        except concurrent.futures.TimeoutError:
            logger.warning("Timeout excedido para: %s", algorithm_name)
            return AlgorithmResult(
                steps=[],
                result=None,
                metadata={
                    "error": True,
                    "error_message": (
                        f"Tempo limite excedido ({settings.TIMEOUT_SECONDS}s). "
                        "Tente números menores."
                    )
                }
            )



class AlgorithmController:
    """Controller que orquestra a execução entre Model e View."""

    def __init__(self, algorithm_name: str):
        try:
            config = AlgorithmRegistry.get(algorithm_name)
        except ValueError as err:
            raise ValueError(f"Algoritmo desconhecido: {algorithm_name}") from err

        self.model_class: Type[BaseAlgorithm] = config["model"]
        self.view_class: Type[BaseView] = config["view"]
        self.algorithm_name = algorithm_name

    @property
    def params(self):
        """Retorna os parâmetros do modelo."""
        return self.model_class.get_params()

    @property
    def input_format_latex(self):
        """Retorna o formato de entrada em LaTeX."""
        return self.model_class.input_format_latex

    def validate_inputs(self, raw_inputs: dict[str, str]) -> tuple[bool, dict]:
        """Valida todos os inputs usando o validador unificado."""
        return InputValidator.validate_all(raw_inputs, self.params)

    def execute(self, raw_inputs: dict[str, str]) -> None:
        """
        Valida, executa e renderiza o algoritmo.

        Este é o método principal que:
        1. Valida os inputs
        2. Instancia o Model com os valores validados
        3. Executa o algoritmo
        4. Renderiza o resultado via View
        """
        # Validação
        is_valid, result = self.validate_inputs(raw_inputs)

        if not is_valid:
            for error in result.get("errors", []):
                st.error(error)
            return

        # Execução do Model (Cached)
        algorithm_result = _run_algorithm_cached(self.algorithm_name, result)

        # Renderização via View
        view = self.view_class()
        view.render(algorithm_result)
