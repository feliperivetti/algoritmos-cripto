import math

from src.models.base import AlgorithmResult, BaseAlgorithm, ParamConfig
from src.models.validators import validate_odd, validate_positive


class FermatModel(BaseAlgorithm):
    """Algoritmo de Fermat para fatoração."""

    name = "Algoritmo de Fermat"
    description = "Fatora um número ímpar usando diferença de quadrados."
    input_format_latex = r"\text{Aplica o Algoritmo de Fermat para } N"

    @classmethod
    def get_params(cls) -> list[ParamConfig]:
        return [
            ParamConfig(name="n", label="N", validations=[validate_positive, validate_odd]),
        ]

    def __init__(self, n: int):
        self.n = n

    def solve(self) -> AlgorithmResult:
        steps = []
        n = self.n

        x = math.isqrt(n)
        x_squared = x * x
        y = 0
        z = n - x_squared + y * y

        steps.append({"n": n, "x": x, "y": y, "z": z})

        while z != 0:
            x += 1
            x_squared = x * x
            diff = x_squared - n

            if diff < 0:
                continue

            y = math.isqrt(diff)
            z = n - x_squared + y * y
            steps.append({"n": "-", "x": x, "y": y, "z": z})

        factor1 = x - y
        factor2 = x + y
        is_prime = (factor1 == 1 or factor2 == 1)

        return AlgorithmResult(
            steps=steps,
            result={"factor1": factor1, "factor2": factor2},
            metadata={
                "factor1": factor1,
                "factor2": factor2,
                "is_prime": is_prime,
                "n": self.n,
            }
        )
