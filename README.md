# Web Scraping - Atualização do Rol de Procedimentos da ANS

Este projeto realiza web scraping em Python utilizando a biblioteca Selenium para acessar o site da Agência Nacional de Saúde Suplementar (ANS), baixar os arquivos PDF dos Anexos I e II referentes ao Rol de Procedimentos e Eventos em Saúde, e compactá-los em um único arquivo `.zip`.

---

## Objetivo do Teste

**TESTE DE WEB SCRAPING**

O objetivo é automatizar o processo de:

1. Acessar a URL:
   - https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos

2. Localizar e realizar o **download dos PDFs** correspondentes aos:
   - Anexo I
   - Anexo II

3. Compactar os arquivos baixados em um **arquivo ZIP**.

---

---

## Projeto com BeautifulSoup

Este script realiza o scraping utilizando apenas requisições HTTP com `requests` e parsing de HTML com `BeautifulSoup`, sem precisar abrir um navegador.

### Bibliotecas utilizadas:
- `requests` - faz a requisição ao site da ANS
- `beautifulsoup4` - extrai os links dos arquivos PDF da página HTML
- `zipfile` - compacta os arquivos

---

## Estrutura do Projeto

```
.
├── install_requirements_bs.py      # Instala as dependências necessárias para BeautifulSoup
├── scraping.py                     # Script principal com BeautifulSoup
├── downloads/                      # Pasta onde os PDFs serão salvos
├── TesteGabrielMedeiros.zip        # Arquivo gerado com os PDFs compactados
```

---

## Como Executar

### 1. Instalar as dependências (uma única vez):
Execute o script a seguir para instalar automaticamente as bibliotecas necessárias:

```bash
python install_requirements_bs.py
```

### 2. Rodar o script principal:

```bash
python scraping.py
```

O script fará:
- Acesso direto à página da ANS
- Busca e filtragem de links PDF de Anexo I e II
- Download dos arquivos para a pasta `downloads/`
- Verificação dos arquivos baixados
- Geração do arquivo `TesteGabrielMedeiros.zip`

---

## Funcionalidade das Funções

- **`pdf_links()`**
  - Realiza uma requisição GET para a página da ANS
  - Analisa o HTML com `BeautifulSoup`
  - Busca por todas as tags `<a>` com links que terminam em `.pdf` e contenham "Anexo_I" ou "Anexo_II"

- **`download_pdfs(links, destination_folder)`**
  - Faz o download de cada PDF e salva na pasta local
  - Exibe mensagens de sucesso ou erro para cada arquivo

- **`check_files(files)`**
  - Verifica a existência dos arquivos após o download

- **`zip_files(files, zip_name)`**
  - Compacta os arquivos baixados em um único arquivo `.zip`


---

## Tecnologias Utilizadas (Resumo)

- **Python**: linguagem principal do projeto
- **Requests**: para baixar o HTML da página e os arquivos PDF
- **BeautifulSoup**: para fazer parsing do HTML e extrair os links
- **Zipfile**: compacta os arquivos baixados em um único `.zip`
- **OS**: manipulação de diretórios e verificação de arquivos

---

## Projeto com Selenium

## Requisitos

Antes de rodar o script principal, é necessário instalar as dependências do projeto. Isso pode ser feito com o script `install_requirements.py`, que instala automaticamente as bibliotecas necessárias.

### Bibliotecas utilizadas:
- `selenium` - automação do navegador
- `webdriver-manager` - gerenciamento automático do driver do Chrome
- `requests` - download dos arquivos PDF

---

## Estrutura do Projeto

```
.
├── install_requirements.py       # Instala as dependências necessárias
├── scraping.py                   # Script principal que executa o scraping
├── downloads/                    # Pasta onde os PDFs serão salvos
├── TesteGabrielMedeiros.zip      # Arquivo gerado com os PDFs compactados
```

---

## Como Executar

### 1. Instalar as dependências (uma única vez):
Execute o script a seguir para instalar automaticamente as bibliotecas necessárias:

```bash
python install_requirements.py
```

### 2. Rodar o script principal:

```bash
python scraping.py
```

O script fará:
- Abertura do navegador e acesso ao site da ANS
- Identificação dos links para os PDFs dos Anexos I e II
- Download dos arquivos para a pasta `downloads/`
- Verifica se os arquivos foram salvos corretamente
- Gera o arquivo compactado `TesteGabrielMedeiros.zip`

---

## Detalhes Técnicos

### `install_requirements.py`
Script que verifica se as bibliotecas `selenium`, `webdriver-manager` e `requests` estão instaladas. Se não estiverem, instala automaticamente via `pip`:

```python
required_packages = ['selenium', 'webdriver-manager', 'requests']
```

---

### `scraping_ans.py`
Script principal:

1. **Configura o navegador** com opção de download para a pasta `downloads`.
2. **Navega até a URL da ANS** e captura os links dos arquivos PDF que contêm "Anexo_I" ou "Anexo_II".
3. **Faz o download** dos arquivos para a pasta local.
4. **Verifica** se os arquivos foram baixados corretamente.
5. **Compacta** os arquivos em `TesteGabrielMedeiros.zip`.

---

## Funcionalidade das Funções

- **`browser_config(download_dir)`**
  - Configura o Chrome para abrir com tamanho fixo de janela e definir uma pasta padrão para downloads.
  - Inicializa o WebDriver do Chrome automaticamente via `webdriver-manager`.

- **`pdf_links(driver)`**
  - Acessa o site da ANS.
  - Coleta todos os links da página e filtra apenas os que são PDFs contendo "Anexo_I" ou "Anexo_II" no nome.

- **`download_pdfs(links, destination_folder)`**
  - Faz download de cada link PDF e salva na pasta especificada.
  - Imprime mensagens de sucesso ou erro para cada arquivo baixado.

- **`check_files(files)`**
  - Verifica se cada arquivo informado realmente existe na pasta de download.
  - Imprime uma lista de arquivos encontrados ou ausentes.

- **`zip_files(files, zip_name)`**
  - Recebe os arquivos baixados e compacta todos em um único arquivo `.zip` com o nome informado.

---

## Tecnologias Utilizadas (Resumo)

- **Python**: linguagem principal do projeto.
- **Selenium**: automação de navegador para acessar e interagir com o site da ANS.
- **WebDriver Manager**: instala e gerencia automaticamente o ChromeDriver.
- **Requests**: realiza o download direto dos arquivos PDF via HTTP.
- **Zipfile**: biblioteca padrão do Python para criar arquivos .zip.
- **OS / TIME**: manipulação de sistema de arquivos e pausas na execução para esperar carregamento da página.

---

## Autor
Gabriel Medeiros

Este projeto foi desenvolvido como parte de um teste técnico envolvendo Web Scraping em Python.
