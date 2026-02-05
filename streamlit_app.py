import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
# Isso garante que "import src.x" funcione corretametne no Streamlit Cloud
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.app import main

if __name__ == "__main__":
    main()
