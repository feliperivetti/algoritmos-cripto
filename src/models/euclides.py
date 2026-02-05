from src.models.base import AlgorithmResult, BaseAlgorithm, ParamConfig


def validate_non_zero(value: int) -> tuple[bool, str]:
    """Valida que o valor não seja zero."""
    if value == 0:
        return False, "O valor não pode ser zero."
    return True, ""


class EuclidesModel(BaseAlgorithm):
    """Algoritmo Euclidiano Estendido - Calcula MDC e coeficientes de Bézout."""

    name = "Euclides Estendido"
    description = "Calcula o MDC e os coeficientes α e β da identidade de Bézout."
    input_format_latex = r"\text{Calcula } \mathrm{MDC}(A, B)"

    @classmethod
    def get_params(cls) -> list[ParamConfig]:
        return [
            ParamConfig(name="a", label="A", validations=[validate_non_zero]),
            ParamConfig(name="b", label="B", validations=[validate_non_zero]),
        ]

    def __init__(self, a: int, b: int):
        # Garante a >= b para o algoritmo
        if abs(b) > abs(a):
            a, b = b, a
        self.a = a
        self.b = b

    def _euclidean_division(self, a: int, b: int) -> tuple[int, int]:
        """Divisão euclidiana com resto positivo."""
        q = a // b
        r = a % b
        if r < 0:
            q += 1
            r -= b
        return q, r

    def solve(self) -> AlgorithmResult:
        steps = []
        a, b = self.a, self.b

        # Inicialização das linhas
        x_prev, x_curr = 1, 0
        y_prev, y_curr = 0, 1

        steps.append({"resto": a, "quociente": "-", "x": x_prev, "y": y_prev})
        steps.append({"resto": b, "quociente": "-", "x": x_curr, "y": y_curr})

        while b != 0:
            q, r = self._euclidean_division(a, b)

            x_new = x_prev - q * x_curr
            y_new = y_prev - q * y_curr

            if r == 0:
                steps.append({"resto": r, "quociente": q, "x": "-", "y": "-"})
            else:
                steps.append({"resto": r, "quociente": q, "x": x_new, "y": y_new})

            a, b = b, r
            x_prev, x_curr = x_curr, x_new
            y_prev, y_curr = y_curr, y_new

        # O MDC é o último valor de 'a' (que era 'b' antes da última iteração)
        mdc = a

        return AlgorithmResult(
            steps=steps,
            result=mdc,
            metadata={
                "mdc": mdc,
                "alpha": x_prev,
                "beta": y_prev,
                "original_a": self.a,
                "original_b": self.b,
            },
        )
