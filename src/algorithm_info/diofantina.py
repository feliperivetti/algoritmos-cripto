"""
Informação do algoritmo Equação Diofantina.
"""

INFO = {
    "icon": "📐",
    "short": "Resolve equações lineares com soluções inteiras",
    "description": """
Uma **Equação Diofantina Linear** tem a forma:

$$A \\cdot X + B \\cdot Y = C$$

O algoritmo encontra todas as soluções inteiras (se existirem).

**Condição de existência:** A equação tem solução se e somente se
MDC(A, B) divide C.

**Quando usar:**
- Problemas de divisibilidade
- Distribuição de recursos inteiros
- Criptografia (RSA)
""",
    "example": "Exemplo: 12X + 8Y = 4 → X₀ = -1, Y₀ = 2",
}
