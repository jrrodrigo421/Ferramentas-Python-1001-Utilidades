import sys
from cx_Freeze import setup, Executable

# Dependências do script
build_exe_options = {
    "packages": ["pytube"],
    "include_files": ["icone.png"]
}

# Configuração do executável
exe = Executable(
    script="donwVideo.py",
    base="Console",
    icon="icone.png"
)

# Cria o executável
setup(
    name="downVideo",
    version="1.0",
    description="Download de videos do Youtube",
    options={"build_exe": build_exe_options},
    executables=[exe]
)
