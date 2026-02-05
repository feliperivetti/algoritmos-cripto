"""
Informação do algoritmo Achar um Fator.
"""

INFO = {
    "icon": "🔍",
    "short": "Encontra um fator não-trivial de um número",
    "description": """
Este algoritmo utiliza o **Método ρ (rho) de Pollard** para encontrar
um fator não-trivial de um número composto.

Usa a sequência: $x_{n+1} = x_n^2 + 1 \\mod N$

E calcula: $d = MDC(|x_i - x_j|, N)$

**Quando usar:**
- Fatoração de números grandes
- Quando Fermat não é eficiente
- Análise de segurança criptográfica
""",
    "example": "Exemplo: Fator de 91 = 7 (91 = 7 × 13)",
}
