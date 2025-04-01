package org.gabrielM.service;

import org.gabrielM.model.PdfFile;

import java.io.File;
import java.io.FileOutputStream;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class DownloadService {

    //Método para fazer download dos anexos
    public List<File> download(List<PdfFile> pdfLinks, String folderPath) {
        List<File> downloadedFiles = new ArrayList<>();
        HttpClient client = HttpClient.newHttpClient();

        for (PdfFile pdf : pdfLinks) {
            try {
                HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create(pdf.getUrl()))
                        .build();

                HttpResponse<byte[]> response = client.send(request, HttpResponse.BodyHandlers.ofByteArray());

                File file = Paths.get(folderPath, pdf.getFilename()).toFile();
                try (FileOutputStream fos = new FileOutputStream(file)) {
                    fos.write(response.body());
                }

                downloadedFiles.add(file);
                System.out.println("PDF baixado com sucesso: " + file.getAbsolutePath());
            } catch (Exception e) {
                System.out.println("Erro ao tentar baixar: " + pdf.getUrl() + "-" + e.getMessage());
            }
        }
        return downloadedFiles;
    }
}


