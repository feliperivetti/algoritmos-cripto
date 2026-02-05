"""
Informação do algoritmo Pseudoprimo Forte.
"""

INFO = {
    "icon": "🛡️",
    "short": "Teste probabilístico de primalidade",
    "description": """
O **Teste de Pseudoprimo Forte** (Miller-Rabin) verifica se um número 
é provavelmente primo.

Decompõe n-1 como: $n - 1 = 2^k \\cdot q$ (q ímpar)

E verifica condições baseadas nas potências de uma base `b`.

**Quando usar:**
- Verificar primalidade de números grandes
- Gerar primos para criptografia
- Cada teste reduz a chance de falso positivo

**Nota:** Se o teste indica "composto", é definitivo. 
Se indica "pseudoprimo forte", há uma pequena chance de erro.
""",
    "example": "Exemplo: 341 com base 2 → É pseudoprimo forte (mas é 11×31)",
}
