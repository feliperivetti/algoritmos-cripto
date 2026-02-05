class CryptoAppError(Exception):
    """Exceção base para todas as exceções da aplicação."""
    pass


class AlgorithmNotFoundError(CryptoAppError):
    """Levatada quando um algoritmo solicitado não é encontrado no registro."""
    def __init__(self, algorithm_name: str):
        self.algorithm_name = algorithm_name
        super().__init__(f"Algoritmo não encontrado: {algorithm_name}")


class CalculationTimeoutError(CryptoAppError):
    """Levantada quando um cálculo excede o tempo limite configurado."""
    def __init__(self, timeout_seconds: int):
        self.timeout_seconds = timeout_seconds
        super().__init__(f"Tempo limite excedido ({timeout_seconds}s).")
