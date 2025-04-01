package org.gabrielM.service;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.List;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class ZipService {

    //Método para compactar os anexos
    public void createZip(List<File> files, String zipPaath){
        try (FileOutputStream fos = new FileOutputStream(zipPaath);
             ZipOutputStream zos = new ZipOutputStream(fos)){

            for (File file: files){
                ZipEntry entry = new ZipEntry(file.getName());
                zos.putNextEntry(entry);

                try (FileInputStream fis = new FileInputStream(file)){
                    fis.transferTo(zos);

                }
                zos.closeEntry();
            }

            System.out.println("Arquivos compactados em: " + zipPaath);

        } catch (Exception e){
            System.out.println("Erro ao criar ZIP: " + e.getMessage());
        }

    }
}
