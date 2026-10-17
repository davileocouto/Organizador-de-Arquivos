from datetime import datetime
from  pathlib import  Path
import shutil
organizador  = Path("organizador.zip")
pasta = Path("Arquivos Organizados")
logs = Path(pasta/"registro.log")
shutil.unpack_archive(organizador, pasta)
extensoes = []
num_arquivos = 0
for arquivo in list(pasta.iterdir()):
    if arquivo.is_file():
        if arquivo.suffix == "":
            pasta_org = Path(pasta/f"Arquivos sem Extensão")
            pasta_org.mkdir(exist_ok=True)
            shutil.move(arquivo, pasta_org)
        if "." in arquivo.suffix:
            extensao = arquivo.suffix
            pasta_org = Path(pasta/f"Arquivos {extensao}")
            pasta_org.mkdir(exist_ok=True)
            shutil.move(arquivo, pasta_org)
        if extensao not in extensoes:
            extensoes.append(extensao)
        num_arquivos += 1
        with open (logs, 'a', encoding='utf-8') as log:
            log.write(f'\n{datetime.now().strftime("%d/%m/%Y às %H:%M - ")}"{arquivo.name}" movido para a pasta "{pasta_org.name}".')
print(f"\n{"="*64}\n\nNúmero total de arquivos organizados: {num_arquivos}\n\nTipos de extensões localizadas: {", ".join(extensoes)}\n\n{"="*64}\n")


