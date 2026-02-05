"""
Informação do algoritmo de Fermat.
"""

INFO = {
    "icon": "🎯",
    "short": "Fatora números usando diferença de quadrados",
    "description": """
O **Método de Fatoração de Fermat** baseia-se na representação de um 
número ímpar N como diferença de dois quadrados:

$$N = a^2 - b^2 = (a+b)(a-b)$$

**Quando usar:**
- Fatorar números ímpares compostos
- Especialmente eficiente quando os fatores são próximos
- Análise de segurança de chaves RSA
""",
    "example": "Exemplo: 143 = 12² - 1² = (12+1)(12-1) = 13 × 11",
}
