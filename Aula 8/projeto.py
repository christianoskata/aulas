import subprocess
import sys
import os
import shutil

def criar_venv(venv_dir):
    """Cria um ambiente virtual no diretório especificado."""
    subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
    print(f"Ambiente virtual criado em: {venv_dir}")


def instalar_pacote(venv_dir, pacote):
    """Instala um pacote no ambiente virtual."""
    # Determina o caminho do pip dentro do venv
    pip_path = os.path.join(venv_dir, "bin", "pip") if os.name != 'nt' else os.path.join(venv_dir, "Scripts", "pip")
    print(pip_path)
    # Instala o pacote
    subprocess.run([pip_path, "install", pacote], check=True)
    print(f"Pacote '{pacote}' instalado no ambiente virtual.")


if __name__ == "__main__":
    venv_dir = "projeto"
    pacote = "requests"
    #os.path.exists(path)
    if os.path.isdir(venv_dir):
        print("O diretório existe.")
        shutil.rmtree(venv_dir)
    else:
        print("O diretório não existe.")
        criar_venv(venv_dir)
        instalar_pacote(venv_dir, pacote)
