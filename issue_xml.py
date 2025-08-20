import time, re, os
import wget
from reports import*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
error_xml_list = []
error_pdf_list = []

def get_pdf(diretorio, xml_link, link, pasta, error_pdf_list):
    '''
    Função para baixar pdf
    '''
    pdf_link = xml_link.replace('?format=xml','?format=pdf')
    lang = xml_link.split('lang=')[1]
    pdf_name = xml_link.replace(f'{link}a','')
    pdf_name = pdf_name.split('?format=')[0] + f"_{lang}.pdf"
    alterar = re.sub(r"[(:\(\)<>?/\\|@+)]", "", pdf_name)
    full_name = re.sub(r"\s+", "_", alterar)
    full_name = full_name.replace("format=xml",'.pdf')
    path_org_pdf = os.path.join(diretorio, 'PDF')
    path_final_pdf = os.path.join(path_org_pdf,pasta)
    if not os.path.exists(path_final_pdf):
        os.makedirs(path_final_pdf)
    out_pdf = os.path.join(path_final_pdf, full_name)
    if not os.path.exists(out_pdf):
        try:
            wget.download(pdf_link, out_pdf)
        except Exception as e:
            print(f'Erro: {e}')
            error_pdf_list.append(pdf_link)
    else:
        print('\nPDF já existe.')

def get_issue(diretorio, link, issue_link, pasta, saveMode):
    '''
    Função para baixar o xml de cada artigo
    '''
    firefox_options = Options()
    firefox_options.add_argument('-lang=pt-BR')
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(issue_link)
    #Botão de aceitar cookies
    try:
        cookies = driver.find_element_by_class_name('alert-cookie-notification')
        #Clicando para fechar o aviso
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[7]/a')
            )).click()
    except:
        pass
    time.sleep(1)
    #try to find h1 tag, if not, pass
    try:
        journal = driver.find_element(By.TAG_NAME,'h1').text
        publisher = driver.find_element(By.CLASS_NAME,'namePlublisher').text
        print(f'\n- Revista: {journal}\n- Publicação de: {publisher}\n')
        table = driver.find_element(By.CLASS_NAME,'table')
        tbody = table.find_element(By.TAG_NAME,'tbody')
        links = tbody.find_elements(By.TAG_NAME,'tr')
        for article in links:
            try:
                article_links = article.find_elements(By.TAG_NAME,'a')
                article_links = [link for link in article_links if 'format=pdf' in link.get_attribute("href")]
                for article_link in article_links:
                    xml_link = article_link.get_attribute("href").replace('format=pdf', 'format=xml')
                    xml_link = re.sub("(\?[a-z]+=[a-z]+$)","?format=xml", xml_link)
                    lang = xml_link.split('lang=')[1]
                    xml_name = xml_link.replace(f'{link}a','')
                    xml_name = xml_name.split('?format=')[0] + f"_{lang}.xml"
                    alterar = re.sub(r"[(:\(\)<>?/\\|@+)]", "", xml_name)
                    full_name = re.sub(r"\s+", "_", alterar)
                    path_org = os. path. join(diretorio, 'XML')
                    path_final = os.path.join(path_org, pasta)
                    if not os.path.exists(path_final):
                        os.makedirs(path_final)
                    out_xml = os.path.join(path_final, full_name)
                    if not os.path.exists(out_xml):
                        try:
                            print(f'\nBaixando XML: {xml_link}')
                            wget.download(xml_link, out_xml)
                        except Exception as e:
                            print(f'Erro: {e}')
                            error_xml_list.append(xml_link)
                    else:
                        print('\nXML já existe.')
                    if saveMode == 2:
                        get_pdf(diretorio, xml_link, link, pasta, error_pdf_list)
                    else:
                        pass
            except Exception as e:
                print(f'Erro ao acessar o artigo: {e}')
                print('\nsem link')
        if len(error_xml_list)!=0:
            report_erro (path_final, error_xml_list, saveMode)
        if len(error_pdf_list)!=0:    
            report_erro_pdf(pasta, error_pdf_list,saveMode)
    except Exception as e:
        print(f'\nErro: {e}')
        print(f'\nNão foi possível encontrar dados para {issue_link}')
    # Fechando o navegador
    driver.quit()

