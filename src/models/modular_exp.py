from src.models.base import BaseAlgorithm, AlgorithmResult, ParamConfig


def validate_non_zero(value: int) -> tuple[bool, str]:
    """Valida que o valor não seja zero."""
    if value == 0:
        return False, "O valor não pode ser zero."
    return True, ""


class ModularExpModel(BaseAlgorithm):
    """Exponenciação Modular - Calcula a^b mod n."""
    
    name = "Exponenciação Modular"
    description = "Calcula a^b mod n encontrando o ciclo das potências."
    input_format_latex = r"\text{Calcula: } A^B \bmod N"
    
    @classmethod
    def get_params(cls) -> list[ParamConfig]:
        return [
            ParamConfig(name="a", label="A", validations=[validate_non_zero]),
            ParamConfig(name="b", label="B", validations=[validate_non_zero]),
            ParamConfig(name="n", label="N", validations=[validate_non_zero]),
        ]
    
    def __init__(self, a: int, b: int, n: int):
        self.a = a
        self.b = b
        self.n = n
    
    def _find_cycle(self) -> tuple[dict[int, int], int]:
        """Encontra o ciclo das potências de a mod n."""
        remainders = {1: self.a % self.n}
        
        i = 2
        while True:
            remainder = (remainders[i - 1] * self.a) % self.n
            
            # Ciclo encontrado
            if remainder in remainders.values():
                cycle_length = i - 1
                break
            
            remainders[i] = remainder
            i += 1
        
        # Adiciona expoente 0
        remainders[0] = 1
        
        return remainders, cycle_length
    
    def solve(self) -> AlgorithmResult:
        remainders, cycle_length = self._find_cycle()
        
        # Prepara passos para exibição
        steps = []
        for exp, rem in sorted(remainders.items()):
            if exp > 0:  # Não mostra expoente 0
                steps.append({"expoente": exp, "resto": rem})
        
        # Calcula resultado final
        quotient = self.b // cycle_length
        remainder_exp = self.b % cycle_length
        
        # Valor do ciclo (primeira potência que repete)
        cycle_value = remainders[cycle_length]
        
        # Resultado final
        result = pow(self.a, self.b, self.n)
        
        return AlgorithmResult(
            steps=steps,
            result=result,
            metadata={
                "a": self.a,
                "b": self.b,
                "n": self.n,
                "cycle_length": cycle_length,
                "cycle_value": cycle_value,
                "quotient": quotient,
                "remainder_exp": remainder_exp,
                "remainders": remainders,
            }
        )
