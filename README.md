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
4. Um teste adicional de checagem de arquivos baixados foi realizado

Com o intuito de demonstrar variadas opções para resolução do teste, adotou-se três diferentes maneiras possíveis de realizar **Web Scraping.**  
Em **Python** o código para **web scraping** foi desenvolvido com duas opções de libs distintas, BeautifulSoup e Selenium. O **web scraping** com BeautifulSoup se mostra mais rápido porque é um framework adequado para páginas estáticas. Selenium é adequado para páginas dinâmicas e requer instalação de drives como o ChromeDrive, trata-se de uma ferramenta de automação utilizada no navegador, você poderá notar que o código com Selenium tem execução bem mais lenta quando comparado ao código com  BeautifulSoup. Em termos de performance e por se tratar de uma página estática, recomenda-se utilizar BeautifulSoup.
Ademais, também foi desenvolvido um código para **web scraping** utilizado Java a partir da biblioteca Jsoup, o código está estruturado na arquitetura MVC.

# Baixar Projeto
Para fazer download do projeto para sua máquina execute via CMD:

```
git clone https://github.com/gabriel-afd/1-WebScraping.git
```

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

### `scraping.py`
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
---

## Projeto com Java

O projeto em Java foi estruturado seguindo o padrão de arquitetura **MVC (Model-View-Controller)** para promover uma organização clara e separação de responsabilidades.

### Estrutura de Pacotes:

- **`model`**
  - **Classe `PdfFile`**: representa um PDF com sua URL e nome de arquivo. Contém métodos para obter e definir esses dados. Também encapsula a lógica para extrair o nome do arquivo a partir da URL.

- **`controller`**
  - **Classe `DownloadController`**: orquestra toda a execução do processo. Cria a pasta de downloads, chama o `ScraperService` para obter os links, o `DownloadService` para baixar os arquivos, e o `ZipService` para compactar tudo em um ZIP.

- **`service`**
  - **Classe `ScraperService`**: faz scraping da página da ANS usando a biblioteca `Jsoup` e retorna uma lista de objetos `PdfFile` com os links dos PDFs Anexo I e II.
  - **Classe `DownloadService`**: utiliza o `HttpClient` da JDK para baixar os PDFs e salvá-los localmente como arquivos físicos.
  - **Classe `ZipService`**: recebe os arquivos baixados e cria um arquivo `.zip` utilizando a API de compressão da JDK.

---
### Como Executar o Projeto Java:

1. Certifique-se de ter o **Java 22** e o **Maven** instalados.

2. Clone ou baixe o projeto.

3. Compile o projeto com Maven:

```bash
mvn clean package
```

4. Após a compilação, execute a aplicação a partir da classe que contém o método `main` e que instancia o `DownloadController`. Exemplo:

```java
public class Main {
    public static void main(String[] args) {
        new DownloadController().execute();
    }
}
```

5. Execute a aplicação diretamente pela IDE(IntelliJ ou Eclipse):

---

### Tecnologias Utilizadas:

- **Java 22**
- **Jsoup**: biblioteca para fazer parsing e scraping de HTML
- **HttpClient**: cliente HTTP moderno da JDK para requisições
- **Java I/O**: manipulação de arquivos
- **Java Zip**: compactação de arquivos
- **Maven**: gerenciamento do projeto e dependências
 
  


## Autor
Gabriel Medeiros

Este projeto foi desenvolvido como parte de um teste técnico envolvendo Web Scraping em Python.
