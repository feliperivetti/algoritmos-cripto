"""
Componentes de UI reutilizáveis.

Importa todos os componentes para facilitar o uso.
"""

from src.components.cards import render_highlight_box, render_metric_card, render_result_card
from src.components.feedback import render_alert
from src.components.forms import render_execute_button, render_input_group
from src.components.layout import render_divider, render_page_header, render_section_header
from src.components.styles import inject_custom_css
from src.components.theme import Theme

__all__ = [
    "Theme",
    "render_page_header",
    "render_section_header",
    "render_divider",
    "render_metric_card",
    "render_result_card",
    "render_highlight_box",
    "render_alert",
    "render_input_group",
    "render_execute_button",
    "inject_custom_css",
]
