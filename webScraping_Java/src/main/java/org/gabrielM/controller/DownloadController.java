package org.gabrielM.controller;

import org.gabrielM.model.PdfFile;
import org.gabrielM.service.DownloadService;
import org.gabrielM.service.ScraperService;
import org.gabrielM.service.ZipService;

import java.io.File;
import java.util.List;

public class DownloadController {

    private static final String DOWNLOAD_DIR = "downloads";
    private static final String ZIP_FILE = "TesteGabrielMedeiros.zip";

    public void execute(){
        try {
            //Criar pasta de download
            File downloadFolder = new File(DOWNLOAD_DIR);
            if(!downloadFolder.exists()) downloadFolder.mkdirs();

            //Pesquisar Links
            ScraperService scraper = new ScraperService();
            List<PdfFile> pdfLinks = scraper.fetchPdfLinks();

            //Baixar arquivos
            DownloadService downloader = new DownloadService();
            List<File> downloadedFiles = downloader.download(pdfLinks, DOWNLOAD_DIR);

            //Verificar se os arquivos foram baixados
            System.out.println("\nVerificando arquivos");
            for (File file : downloadedFiles){
                if (file.exists()){
                    System.out.println("Encontrado: " + file.getName());
                } else {
                    System.out.println("Não encontrado: " + file.getName());
                }
            }

            //Compactar arquivos em ZIP
            ZipService zipService = new ZipService();
            zipService.createZip(downloadedFiles,ZIP_FILE);

        } catch (Exception e){
            System.out.println("Erro geral: " + e.getMessage());
        }
    }
}
