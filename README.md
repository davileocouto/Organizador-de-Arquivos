# Organizador de Arquivos | File Organizer

A Python utility that extracts files from `.zip` archives and automatically organizes them into folders based on their file extensions.

Uma ferramenta em Python que extrai arquivos de arquivos `.zip` e os organiza automaticamente em pastas de acordo com suas extensões.

---

## English

### Features

- **Automatic Extraction:** Extracts files from `.zip` archives.
- **Extension-Based Organization:** Sorts files into folders according to their extensions.
- **Nested Directory Support:** Finds files inside subdirectories within the archive.
- **Custom ZIP Path:** Allows users to specify the path of the ZIP archive they want to organize.
- **Extensionless File Support:** Places files without extensions into a dedicated folder.
- **Operation Logging:** Records each file operation in a `.log` file, including the date, time, filename, and destination.
- **Empty Directory Cleanup:** Removes empty directories left after organizing files.
- **Summary Report:** Displays the total number of organized files and the file extensions found.

### Requirements

- Python 3.10 or later recommended.
- No external dependencies are required. The program uses Python's standard library:
  - `datetime`
  - `pathlib`
  - `shutil`

### How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/davileocouto/Organizador-de-Arquivos.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Organizador-de-Arquivos
   ```

3. **Run the program:**

   ```bash
   python main.py
   ```

   Replace `main.py` with the actual Python filename if it differs.

4. **Provide the ZIP file path** when prompted. You can enter a relative or absolute path.

   Example:

   ```text
   D:\Downloads\files.zip
   ```

5. The program extracts and organizes the files, creates the destination folders, records the operations in `registro.log`, and displays a summary in the terminal.

### Example

Suppose the ZIP archive contains the following files:

```text
files.zip
├── photo.png
├── document.pdf
├── spreadsheet.csv
├── README
└── Documents/
    └── report.pdf
```

After running the program, the resulting directory structure will look like this:

```text
Organizador_de_Arquivos/
└── Arquivos Organizados/
    ├── Arquivos PNG/
    │   └── photo.png
    ├── Arquivos PDF/
    │   ├── document.pdf
    │   └── report.pdf
    ├── Arquivos CSV/
    │   └── spreadsheet.csv
    ├── Arquivos sem Extensão/
    │   └── README
    └── registro.log
```

**Note:** The output structure is illustrative. The actual folders depend on the files contained in the selected ZIP archive.

---

## Português

### Funcionalidades

- **Extração Automática:** Extrai arquivos de arquivos `.zip`.
- **Organização por Extensão:** Separa os arquivos em pastas de acordo com suas extensões.
- **Suporte a Subpastas:** Localiza arquivos dentro de subpastas presentes no arquivo ZIP.
- **Caminho Personalizado:** Permite informar o caminho do arquivo ZIP que será organizado.
- **Suporte a Arquivos sem Extensão:** Direciona arquivos sem extensão para uma pasta específica.
- **Registro de Operações:** Registra cada operação em um arquivo `.log`, incluindo data, horário, nome do arquivo e destino.
- **Limpeza de Pastas Vazias:** Remove diretórios vazios que sobram após a organização.
- **Resumo da Execução:** Exibe a quantidade total de arquivos organizados e as extensões encontradas.

### Requisitos

- Python 3.10 ou superior recomendado.
- Nenhuma biblioteca externa é necessária. O programa utiliza módulos da biblioteca padrão do Python:
  - `datetime`
  - `pathlib`
  - `shutil`

### Como Usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/davileocouto/Organizador-de-Arquivos.git
   ```

2. **Entre na pasta do projeto:**

   ```bash
   cd Organizador-de-Arquivos
   ```

3. **Execute o programa:**

   ```bash
   python main.py
   ```

   Substitua `main.py` pelo nome real do arquivo Python, caso seja diferente.

4. **Informe o caminho do arquivo ZIP** quando solicitado. Você pode utilizar um caminho absoluto ou relativo.

   Exemplo:

   ```text
   D:\Downloads\arquivos.zip
   ```

5. O programa extrairá e organizará os arquivos, criará as pastas de destino, registrará as operações no arquivo `registro.log` e exibirá um resumo no terminal.

### Exemplo

Imagine que o arquivo ZIP contenha os seguintes arquivos:

```text
arquivos.zip
├── foto.png
├── documento.pdf
├── planilha.csv
├── LEIA-ME
└── Documentos/
    └── relatório.pdf
```

Após a execução, a estrutura ficará semelhante a esta:

```text
Arquivos Organizados/
├── Arquivos PNG/
│   └── foto.png
├── Arquivos PDF/
│   ├── documento.pdf
│   └── relatório.pdf
├── Arquivos CSV/
│   └── planilha.csv
├── Arquivos sem Extensão/
│   └── LEIA-ME
└── registro.log
```

**Observação:** A estrutura apresentada é ilustrativa. As pastas criadas dependem dos arquivos presentes no ZIP selecionado.

---

## License

No license has been specified for this project.
