
from datetime import datetime
from pathlib import Path
import shutil
import time

while True:
    caminho_zip = input("\nDigite o caminho do arquivo ZIP: ").strip().strip('"')
    arquivo_zip = Path(caminho_zip)

    pasta = Path("Arquivos Organizados")
    pasta.mkdir(exist_ok=True)

    logs = Path(pasta / "registro.log")
    shutil.unpack_archive(arquivo_zip, pasta)

    extensoes = []
    num_arquivos = 0

    for arquivo in list(pasta.rglob("*")):
        if arquivo.is_file() and arquivo != logs:
            extensao = arquivo.suffix.lower()

            if extensao == "":
                pasta_org = Path(pasta / "Arquivos sem Extensão")
            else:
                pasta_org = Path(pasta / f"Arquivos {extensao[1:].upper()}")

            if pasta_org not in arquivo.parents:
                pasta_org.mkdir(exist_ok=True)
                shutil.move(str(arquivo), str(pasta_org / arquivo.name))

                if extensao and extensao not in extensoes:
                    extensoes.append(extensao)

                num_arquivos += 1

                with open(logs, "a", encoding="utf-8") as log:
                    log.write(
                        f'\n{datetime.now().strftime("%d/%m/%Y às %H:%M:%S - ")}'
                        f'"{arquivo.name}" movido para a pasta "{pasta_org}".'
                    )
    for arquivo in sorted(pasta.rglob("*"), reverse=True):
        if arquivo.is_dir() and not any(arquivo.iterdir()):
            arquivo.rmdir()
    print(
        f"\n{'=' * 64}\n\n"
        f"Nome do arquivo: {arquivo_zip.name}\n\n"
        f"Número total de arquivos organizados: {num_arquivos}\n\n"
        f"Tipos de extensões localizadas: {', '.join(ext.upper().lstrip('.') for ext in extensoes)}\n\n"
        f"{'=' * 64}\n"
    )
    time.sleep(0.5)
    input('Aperte "Enter" para continuar\n')
    while True:
        pergunta = int(input("Você deseja continuar?\n\n1. Sim\n2. Não\n\n"))
        match pergunta:
            case 1:
                print("\nRecomeçando...\n")
                finalizou = False
                time.sleep(0.3)
                break
            case 2:
                print("\nFinalizando...\n")
                finalizou = True
                time.sleep(0.3)
                break
            case _:
                print("Digite uma opção entre 1 ou 2!\n\n")
    if finalizou == True:
        break