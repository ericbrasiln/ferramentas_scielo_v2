import os
import re
from xml.etree import ElementTree as ET

# Função para encontrar o link do PDF utilizando xml.etree
def find_pdf_link(entry, linkPDF):
    hrefmap = {"xlink": "http://www.w3.org/1999/xlink"}
    try:
        tree = ET.parse(entry) # Analisa o arquivo XML
        root = tree.getroot()
        journalData = root.find('front')
        articleMeta = journalData.find('article-meta')
        links = articleMeta.findall('self-uri/[@xlink:href]', namespaces=hrefmap) # Encontra a lista com links
        for l in links: # Iteração na lista de links, tranformando-os em strings
            link = l.attrib
            linkStr = str(link)
            linkStr = linkStr.replace("{\'{http://www.w3.org/1999/xlink}href\': '", "")
            linkStr = linkStr.replace("'}","")
            if re.search('script=sci_pdf', linkStr): # Iteração para encontrar o item da lista que contém o caminho para PDF
                pdf =  linkStr
                linkPDF.append(pdf) # Inclui o link na lista linkPDF
            else:
                pass
    except Exception as e: # Se o XML apresentar algum erro em sua estrutura o pdf receberá "Erro no XML"
        pdf = f"Erro no XML: {e}"
        linkPDF.append(pdf) 
