import os
import requests
from bs4 import BeautifulSoup
import zipfile

#Configurações
DOWNLOAD_DIR=os.path.abspath("downloads")
zip_filename = "TesteGabrielMedeiros.zip"
url='https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

#Função para obter os links de PDF utilizando a biblioteca BeautifulSoup
def pdf_links():
    print("Acessando página...")
    response=requests.get(url)
    soup=BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')
    pdfs=[]

    for link in links:
        href = link.get('href')
        if href and href.endswith(".pdf") and ("Anexo_I" in href or "Anexo_II" in href):
            if href.startswith('/'):
                href='https://www.gov.br' + href
            pdfs.append(href)
    print(f"{len(pdfs)} PDFs encontrados.")
    return pdfs

#Função para baixar os arquivos PDF
def download_pdfs(links, destination_folder):
    files = []
    for href in links:
        try:
            filename=os.path.basename(href)
            complete_file=os.path.join(destination_folder, filename)
            response = requests.get(href)
            with open(complete_file, 'wb') as f:
                f.write(response.content)
            files.append(complete_file)
            print(f"PDF baixado com sucesso: {complete_file}")

        except Exception as ex:
            print(f"Erro ao tentar baixar: {href}:{ex}")

    return files

#Função para verificar se os arquivos foram baixados
def check_files(files):
    print("\nVerificando arquivos...")
    for file in files:
        if os.path.exists(file):
            print(f"Encontrado: {os.path.basename(file)}")
        else:
            print(f"Não encontrado: {os.path.basename(file)}")

#Função para compactar os arquivos em ZIP
def zip_files(files, zip_name):
    with zipfile.ZipFile(zip_name,'w') as zipf:
        for file in files:
            zipf.write(file, arcname=os.path.basename(file))
    print(f"Arquivos compactados em: {zip_name}")

#Execução principal
def main():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    links_pdf=pdf_links()
    downloaded_files = download_pdfs(links_pdf, DOWNLOAD_DIR)
    check_files(downloaded_files)
    zip_files(downloaded_files, zip_filename)

if __name__== "__main__":
    main()