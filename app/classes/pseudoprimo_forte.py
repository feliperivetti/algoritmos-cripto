import math, random

import pandas as pd
import streamlit as st

from classes.base_algorithm import BaseAlgorithm, classproperty


class PseudoPrimoForte(BaseAlgorithm):

    @classproperty
    def input_format(cls):
        return r"\text{Verifica se } N \text{ é um pseudoprimo forte na base } B"
    
    @classproperty
    def params(cls):
        params = ["n", "b"]
        return params

    # TODO: Implementar validação de entrada
    # n deve ser um número ímpar e b não deve ser divisível por b
    # eu deveria receber o input_name para testes diferentes pro n e pro b
    @staticmethod
    def validate_input(input_value):
        try:
            input_value = int(input_value)
            if input_value <= 0:
                st.error("Por favor, digite um número inteiro maior que zero.")
                return False
            return True
        
        except ValueError:
            st.error("Por favor, digite um número inteiro válido.")
            return False

    def __init__(self, n, b):
        self.n = n
        self.b = b
        self.k = None
        self.q = None
        self.results = {}

    def decompose_n_minus_1(self):
        k, q = 0, 0
        num = self.n - 1

        while num % 2 == 0:
            num //= 2
            k+=1
        q = num

        st.latex("n - 1 = 2^k \\cdot q")
        st.latex(f"{self.n - 1} = 2^{{{k}}} \\cdot {q}")

        self.k = k
        self.q = q
        return k, q
    
    def solve(self):
        st.write(f"### Decompondo n - 1:")
        self.decompose_n_minus_1()
        i = 0
        r = pow(self.b, self.q, self.n)
        values = [self.b, self.q, r]

        st.write(f"### Aplicando o Algoritmo:")
        while i < self.k:
            st.latex(f"i = {i}: {values[0]}^{{{values[1]}}} \\equiv {values[2]} \\pmod{{{self.n}}}")
            if (i == 0 and r == 1) or (r == self.n - 1):
                st.write(f"### Teste Inconclusivo: {self.n} é um pseudoprimo forte!")
                return True
            i+=1
            values = [r, 2, pow(r, 2, self.n)]
            r = values[2]
        st.write(f"### {self.n} é composto (não é um pseudoprimo forte)")
        return False


if __name__ == "__main__":
    n, b = 697, 42
    teste = PseudoPrimoForte(n, b)
    teste.solve()
