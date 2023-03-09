import zipfile
import os
import tkinter as tk
from tkinter import filedialog


def compactar_pasta(pasta):
    # Cria um objeto ZipFile
    zip_file = zipfile.ZipFile(f"{pasta}.zip", "w")

    # Adiciona todos os arquivos da pasta ao arquivo zip
    for root, dirs, files in os.walk(pasta):
        for file in files:
            zip_file.write(os.path.join(root, file))

    # Fecha o arquivo zip
    zip_file.close()

    print(f"Arquivo {pasta}.zip criado com sucesso!")


def descompactar_pasta():
    # Abre uma janela de seleção de arquivo
    root = tk.Tk()
    root.withdraw()
    pasta = filedialog.askdirectory()

    # Cria um objeto ZipFile com o nome da pasta
    zip_file = zipfile.ZipFile(f"{pasta}.zip", "r")

    # Extrai todos os arquivos da pasta para o diretório atual
    zip_file.extractall()

    # Fecha o arquivo zip
    zip_file.close()

    print(f"Pasta {pasta} descompactada com sucesso!")


# Exemplo de uso
opcao = input("Digite 1 para compactar ou 2 para descompactar: ")
if opcao == "1":
    pasta = input("Digite o caminho da pasta a ser compactada: ")
    compactar_pasta(pasta)
elif opcao == "2":
    descompactar_pasta()
else:
    print("Opção inválida.")
