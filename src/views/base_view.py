from abc import ABC, abstractmethod

import streamlit as st

from src.models.base import AlgorithmResult


class BaseView(ABC):
    """Classe base para views."""

    @abstractmethod
    def render(self, result: AlgorithmResult) -> None:
        pass

    def render_error(self, msg: str) -> None:
        st.error(msg)

    def render_success(self, msg: str) -> None:
        st.success(msg)
