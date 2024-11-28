import os
import sys
from cx_Freeze import setup, Executable

# Caminho dos arquivos de recurso
path = "./asset"
if not os.path.exists(path):
    raise FileNotFoundError(f"O diretório {path} não foi encontrado!")

# Lista de arquivos no diretório 'asset'
asset_list = os.listdir(path)
asset_list_completa = [(os.path.join(path, asset), "asset/" + asset) for asset in asset_list]
print(asset_list_completa)

# Ajuste para verificar o caminho correto de acesso aos arquivos de recursos
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Para quando o executável for gerado
else:
    base_path = os.path.abspath(".")  # Para quando estiver no ambiente de desenvolvimento

# Executáveis
executables = [Executable("main.py")]

# Arquivos a serem incluídos
files = {
    "include_files": asset_list_completa,  # Arquivos de recursos
    "packages": ["pygame"]  # Pacote pygame
}

# Executa o setup
setup(
    name="MountainShooter",
    version="1.0",
    description="Mountain Shooter app",
    options={"build_exe": files},
    executables=executables
)
