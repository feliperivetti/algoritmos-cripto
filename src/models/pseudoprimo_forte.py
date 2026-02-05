from src.models.base import BaseAlgorithm, AlgorithmResult, ParamConfig
from src.models.validators import validate_greater_than_one, validate_odd


class PseudoPrimoForteModel(BaseAlgorithm):
    """Teste de Pseudoprimo Forte - Verifica se N é pseudoprimo forte na base B."""
    
    name = "Pseudoprimo Forte"
    description = "Verifica se N é um pseudoprimo forte na base B."
    input_format_latex = r"\text{Verifica se } N \text{ é um pseudoprimo forte na base } B"
    
    @classmethod
    def get_params(cls) -> list[ParamConfig]:
        return [
            ParamConfig(name="n", label="N", validations=[validate_greater_than_one, validate_odd]),
            ParamConfig(name="b", label="B", validations=[validate_greater_than_one]),
        ]
    
    def __init__(self, n: int, b: int):
        self.n = n
        self.b = b
    
    def _decompose(self, n: int) -> tuple[int, int]:
        """Decompõe n-1 = 2^k * q onde q é ímpar."""
        k = 0
        q = n - 1
        
        while q % 2 == 0:
            q //= 2
            k += 1
        
        return k, q
    
    def solve(self) -> AlgorithmResult:
        steps = []
        n = self.n
        b = self.b
        
        # Verifica se b é múltiplo de n
        if b % n == 0:
            return AlgorithmResult(
                steps=[],
                result=None,
                metadata={
                    "error": True,
                    "error_message": f"B ({b}) não pode ser múltiplo de N ({n}).",
                }
            )
        
        # Decompõe n-1
        k, q = self._decompose(n)
        
        steps.append({
            "tipo": "decomposicao",
            "k": k,
            "q": q,
            "n_minus_1": n - 1,
        })
        
        # Aplica o teste
        i = 0
        r = pow(b, q, n)
        
        iteration_steps = []
        
        while i < k:
            iteration_steps.append({
                "i": i,
                "base": b if i == 0 else r_prev,
                "expoente": q if i == 0 else 2,
                "resultado": r,
            })
            
            # Condição 1: i=0 e r=1
            if i == 0 and r == 1:
                return AlgorithmResult(
                    steps=iteration_steps,
                    result=True,
                    metadata={
                        "k": k,
                        "q": q,
                        "n": n,
                        "b": b,
                        "is_strong_pseudoprime": True,
                        "reason": f"b^q ≡ 1 (mod n)",
                    }
                )
            
            # Condição 2: r = n-1
            if r == n - 1:
                return AlgorithmResult(
                    steps=iteration_steps,
                    result=True,
                    metadata={
                        "k": k,
                        "q": q,
                        "n": n,
                        "b": b,
                        "is_strong_pseudoprime": True,
                        "reason": f"Encontrou r ≡ -1 (mod n) em i={i}",
                    }
                )
            
            i += 1
            r_prev = r
            r = pow(r, 2, n)
        
        # Nenhuma condição satisfeita - é composto
        return AlgorithmResult(
            steps=iteration_steps,
            result=False,
            metadata={
                "k": k,
                "q": q,
                "n": n,
                "b": b,
                "is_strong_pseudoprime": False,
                "reason": f"{n} é composto (não é pseudoprimo forte na base {b})",
            }
        )
