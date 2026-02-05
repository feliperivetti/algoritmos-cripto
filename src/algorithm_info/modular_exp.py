"""
Informação do algoritmo Exponenciação Modular.
"""

INFO = {
    "icon": "⚡",
    "short": "Calcula potências grandes em aritmética modular",
    "description": """
A **Exponenciação Modular** calcula eficientemente:

$$a^b \\mod n$$

O algoritmo encontra um ciclo nas potências de `a` módulo `n` e 
usa isso para calcular o resultado sem computar a potência completa.

**Quando usar:**
- Criptografia RSA e Diffie-Hellman
- Testes de primalidade
- Assinaturas digitais
""",
    "example": "Exemplo: 3¹⁰⁰ mod 7 = 4",
}
