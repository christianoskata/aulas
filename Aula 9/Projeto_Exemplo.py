import subprocess
import sys
import os


def criar_venv(venv_dir):
    """Cria um ambiente virtual no diretório especificado."""
    subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
    print(f"Ambiente virtual criado em: {venv_dir}")


def instalar_requisitos(venv_dir, requirements_file):
    """Instala pacotes a partir de um arquivo requirements.txt no ambiente virtual."""
    # Determina o caminho do pip dentro do venv
    # nt = Windows
    if os.name != 'nt':
        pip_path = os.path.join(venv_dir, "bin", "pip")
    else:
        os.path.join(venv_dir, "Scripts", "pip")

    # Instala os pacotes listados no arquivo requirements.txt
    subprocess.run([pip_path, "install", "-r", requirements_file], check=True)
    print(f"Pacotes instalados a partir de '{requirements_file}' no ambiente virtual.")


if __name__ == "__main__":
    venv_dir = "projeto_req"
    # pip freeze > requirements.txt
    requirements_file = "requirements.txt"

    criar_venv(venv_dir)
    instalar_requisitos(venv_dir, requirements_file)
