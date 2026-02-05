from src.models.base import AlgorithmResult, BaseAlgorithm, ParamConfig
from src.models.euclides import EuclidesModel, validate_non_zero


class DiofantinaModel(BaseAlgorithm):
    """Equação Diofantina - Resolve ax + by = c."""

    name = "Equação Diofantina"
    description = "Encontra soluções inteiras para a equação ax + by = c."
    input_format_latex = r"\text{Equação Diofantina: } Ax + By = C"

    @classmethod
    def get_params(cls) -> list[ParamConfig]:
        return [
            ParamConfig(name="a", label="A", validations=[validate_non_zero]),
            ParamConfig(name="b", label="B", validations=[validate_non_zero]),
            ParamConfig(name="c", label="C", validations=[validate_non_zero]),
        ]

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def solve(self) -> AlgorithmResult:
        # Executa Euclides para obter MDC e coeficientes
        euclides = EuclidesModel(self.a, self.b)
        euclides_result = euclides.solve()

        mdc = euclides_result.metadata["mdc"]
        euclides_alpha = euclides_result.metadata["alpha"]
        euclides_beta = euclides_result.metadata["beta"]
        euclides_a = euclides_result.metadata["original_a"]

        # Se Euclides inverteu (porque |b| > |a|), inverte alpha/beta
        if euclides_a != self.a:
            alpha = euclides_beta
            beta = euclides_alpha
        else:
            alpha = euclides_alpha
            beta = euclides_beta

        # Verifica se existe solução
        if self.c % mdc != 0:
            return AlgorithmResult(
                steps=[],
                result=None,
                metadata={
                    "has_solution": False,
                    "reason": f"c ({self.c}) não é divisível pelo MDC ({mdc})",
                    "euclides_result": euclides_result,
                },
            )

        # Calcula solução particular
        divisor = self.c // mdc
        x0 = alpha * divisor
        y0 = beta * divisor

        # Coeficientes da solução geral
        x_coef = self.b // mdc
        y_coef = self.a // mdc

        return AlgorithmResult(
            steps=euclides_result.steps,
            result={"x0": x0, "y0": y0},
            metadata={
                "has_solution": True,
                "mdc": mdc,
                "alpha": alpha,
                "beta": beta,
                "divisor": divisor,
                "x0": x0,
                "y0": y0,
                "x_coef": x_coef,
                "y_coef": y_coef,
                "a": self.a,
                "b": self.b,
                "c": self.c,
                "euclides_result": euclides_result,
            },
        )
