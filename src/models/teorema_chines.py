import math
from functools import reduce

from src.models.base import AlgorithmResult, BaseAlgorithm, ParamConfig
from src.models.euclides import EuclidesModel


def _extended_gcd_inverse(a: int, m: int) -> int:
    """
    Calcula o inverso modular de a mod m usando Euclides Estendido.
    Retorna x tal que a*x ≡ 1 (mod m).
    """
    # Usa o modelo existente de Euclides para consistência
    model = EuclidesModel(a, m)
    result = model.solve()

    # O modelo EuclidesModel(a, m) pode trocar a e m se m > a no __init__.
    # Se trocar, a identidade vira m*alpha + a*beta = 1, e queremos o coef de a (beta).
    # Se não trocar, a*alpha + m*beta = 1, e queremos o coef de a (alpha).
    # Como não temos acesso fácil ao "swapped" flag, replicamos a lógica de check:

    if abs(m) > abs(a):
        # Houve troca internamente no EuclidesModel
        x = result.metadata["beta"]
    else:
        # Não houve troca
        x = result.metadata["alpha"]

    return int(x) % m


class TeoremaChinesModel(BaseAlgorithm):
    """
    Teorema Chinês do Resto (CRT).
    Resolve sistemas de congruências lineares: x ≡ a_i (mod m_i).
    """

    name = "Teorema Chinês do Resto"
    description = "Resolve sistemas de congruências onde os módulos são coprimos 2 a 2."
    input_format_latex = r"x \equiv a_i \pmod{m_i}"

    @classmethod
    def get_params(cls) -> list[ParamConfig]:
        # Para o CRT, precisamos de uma lista dinâmica de equações.
        # Como o BaseAlgorithm espera parâmetros fixos, vamos definir dois campos de texto
        # que esperam valores separados por vírgula.
        return [
            ParamConfig(
                name="a_list", label="Valores de 'a' (separados por vírgula)", validations=[]
            ),
            ParamConfig(
                name="m_list", label="Valores de 'm' (separados por vírgula)", validations=[]
            ),
        ]

    def __init__(self, a_list: str, m_list: str):
        # Converte strings para listas de inteiros
        try:
            self.a_values = [int(x.strip()) for x in a_list.split(",")]
            self.m_values = [int(x.strip()) for x in m_list.split(",")]
        except ValueError:
            # Será tratado na validação ou execução se passar inválido
            self.a_values = []
            self.m_values = []

    def solve(self) -> AlgorithmResult:
        steps = []

        # 1. Validação Básica
        if len(self.a_values) != len(self.m_values):
            return AlgorithmResult(
                steps=[],
                result=None,
                metadata={
                    "error": True,
                    "error_message": "As listas 'a' e 'm' devem ter o mesmo tamanho.",
                },
            )

        if not self.a_values:
            return AlgorithmResult(
                steps=[], result=None, metadata={"error": True, "error_message": "Entrada vazia."}
            )

        # 2. Verifica se módulos são coprimos 2 a 2
        for i in range(len(self.m_values)):
            for j in range(i + 1, len(self.m_values)):
                if math.gcd(self.m_values[i], self.m_values[j]) != 1:
                    return AlgorithmResult(
                        steps=[],
                        result=None,
                        metadata={
                            "error": True,
                            "error_message": (
                                f"Módulos não são coprimos de 2 a 2: "
                                f"gcd({self.m_values[i]}, {self.m_values[j]}) != 1"
                            ),
                        },
                    )

        # 3. Cálculo do Mzão (Produto de todos m_i)
        M = reduce(lambda x, y: x * y, self.m_values)
        steps.append({"step": "Calculo de M", "M": M})

        solution = 0
        details = []

        # 4. Loop principal
        for i, (a_i, m_i) in enumerate(zip(self.a_values, self.m_values, strict=False)):
            M_i = M // m_i

            # Calcula inverso y_i tal que M_i * y_i ≡ 1 (mod m_i)
            # Precisamos tratar m_i=1 (inverso é 0 ou irrelevante)
            if m_i == 1:
                y_i = 0
            else:
                y_i = _extended_gcd_inverse(M_i, m_i)

            term = a_i * M_i * y_i
            solution += term

            details.append(
                {"i": i + 1, "a_i": a_i, "m_i": m_i, "M_i": M_i, "y_i": y_i, "term": term}
            )

            steps.append(
                {
                    "step": f"Termo {i+1}",
                    "equation": f"x ≡ {a_i} mod {m_i}",
                    "M_i": M_i,
                    "y_i": y_i,
                    "calculation": f"{a_i} * {M_i} * {y_i} = {term}",
                }
            )

        final_x = solution % M

        return AlgorithmResult(
            steps=steps,
            result=final_x,
            metadata={"M": M, "solution": final_x, "terms_details": details},
        )
