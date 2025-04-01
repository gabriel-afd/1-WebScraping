package org.gabrielM.service;

import org.gabrielM.model.PdfFile;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ScraperService {

    private static final String BASE_URL = "https://www.gov.br";
    private static final String TARGET_URL = BASE_URL + "/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos";

    //Método para buscar links
    public List<PdfFile> fetchPdfLinks(){
        List<PdfFile> pdfs = new ArrayList<>();
        Document document = null;
        try {
            document = Jsoup.connect(TARGET_URL).get();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        Elements links = document.select("a[href$=.pdf]");

        for (Element link: links){
            String href = link.attr("href");

            if (href != null && !href.isEmpty() && ((href.contains("Anexo_I") || href.contains("Anexo_II")))){
                if(href.startsWith("/")){
                    href = BASE_URL + href;
                }
                pdfs.add(new PdfFile(href));
            }
        }
        System.out.println(pdfs.size() + "PDFs encontrados");
        return pdfs;
    }
}
