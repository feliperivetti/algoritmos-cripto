"""
Informação do algoritmo Euclides Estendido.
"""

INFO = {
    "icon": "🔢",
    "short": "Calcula o MDC e os coeficientes de Bézout",
    "description": """
O **Algoritmo Euclidiano Estendido** calcula o Máximo Divisor Comum (MDC) 
de dois números inteiros e encontra os coeficientes α e β que satisfazem 
a **Identidade de Bézout**:

$$MDC(A, B) = α \\cdot A + β \\cdot B$$

**Quando usar:**
- Encontrar o MDC entre dois números
- Resolver equações diofantinas lineares
- Calcular inversos multiplicativos modulares
""",
    "example": "Exemplo: MDC(48, 18) = 6, com α = -1 e β = 3",
}
