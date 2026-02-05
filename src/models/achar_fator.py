from src.models.base import BaseAlgorithm, AlgorithmResult, ParamConfig
from src.models.validators import validate_greater_than_one


class AcharFatorModel(BaseAlgorithm):
    """Algoritmo Achar um Fator - Encontra um fator de N por divisões sucessivas."""
    
    name = "Achar um Fator"
    description = "Encontra um fator de N testando divisores a partir de 2."
    input_format_latex = r"\text{Calcula um fator de N}"
    
    @classmethod
    def get_params(cls) -> list[ParamConfig]:
        return [
            ParamConfig(name="n", label="N", validations=[validate_greater_than_one]),
        ]
    
    def __init__(self, n: int):
        self.n = n
    
    def solve(self) -> AlgorithmResult:
        steps = []
        n = self.n
        
        factor = None
        f = 2
        steps_count = 0
        
        while f * f <= n:
            steps_count += 1
            if n % f == 0:
                factor = f
                steps.append({"numero": f, "fator": "Sim"})
                break
            else:
                steps.append({"numero": f, "fator": "Não"})
            f += 1
        
        is_prime = factor is None
        
        return AlgorithmResult(
            steps=steps,
            result=factor if not is_prime else n,
            metadata={
                "n": self.n,
                "factor": factor,
                "is_prime": is_prime,
                "steps_count": steps_count if not is_prime else len(steps),
            }
        )
