import os
from time import sleep
import zipfile
import requests
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

#Configurações de pasta e url
DOWNLOAD_DIR = os.path.abspath("downloads")
zip_filename="TesteGabrielMedeiros.zip"
url='https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'


#Configuração do navegador
def browser_config(download_dir):
    prefs = {"download.default_directory": download_dir}
    opts = Options()
    opts.add_argument('--window-size=1920,1080')
    opts.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts,

    )
    return driver

#Função para obter links de download do PDF
def pdf_links(driver):
    driver.get(url) #Request GET para o site
    sleep(3)
    links = driver.find_elements(By.TAG_NAME, 'a')
    pdfs=[]
    for link in links:
        href = link.get_attribute("href")
        if href and href.endswith(".pdf") and ("Anexo_I" in href or "Anexo_II" in href):#Filtrando hrefs que terminam com ".pdf" e são do tipo "Anexo_I" ou "Anexo_II"
            pdfs.append(href)
    return pdfs

#Função para baixar os PDFs
def download_pdfs(links,destination_folder):
    files=[]
    for href in links:
        try:
            filename = os.path.basename(href)
            complete_file = os.path.join(destination_folder,filename)
            response = requests.get(href)
            with open(complete_file, 'wb') as f:
                f.write(response.content)
            files.append(complete_file)
            print(f"PDF baixado com sucesso: {complete_file}")

        except Exception as ex:
            print(f"Erro ao tentar baixar arquivos:{href}: {ex}")
    return files

#Função para validar se os arquivos foram baixados para a pasta designada
def check_files(files):
    print("\nVerificando arquivos:")
    for file in files:
        if os.path.exists(file):
            print(f"Encontrado: {os.path.basename(file)}")
        else:
            print(f"Não encontrado: {os.path.basename(file)}")

#Função para compactar arquivos em ZIP
def zip_files(files, zip_name):
    with zipfile.ZipFile(zip_name,'w') as zipf:
        for file in files:
            zipf.write(file, arcname=os.path.basename(file))
    print(f"Arquivos compactados em: {zip_name}")

def main():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    driver = browser_config(DOWNLOAD_DIR)
    try:
        links_pdf = pdf_links(driver)
    finally:
        driver.quit()

    download_files = download_pdfs(links_pdf, DOWNLOAD_DIR)
    check_files(download_files)
    zip_files(download_files, zip_filename)

if __name__ == "__main__":
    main()