package org.gabrielM.model;


public class PdfFile {

    private String url;
    private String filename;


    public PdfFile(String href) {

        if (href == null || href.isEmpty()){
            throw new IllegalArgumentException("URL não pode ser null");
        }
        this.url = href;
        this.filename = url.substring(url.lastIndexOf("/")+1);
    }

    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
}
