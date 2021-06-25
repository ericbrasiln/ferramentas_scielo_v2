import time, re, os
import wget
from reports import*
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
error_xml_list = []
error_pdf_list = []

def get_pdf(diretorio, xml_link, link, pasta, error_pdf_list):
    '''
    Função para baixar pdf
    '''
    pdf_link = xml_link.replace('?format=xml','?format=pdf')
    pdf_name = xml_link.replace(f'{link}a','')
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
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
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
    journal = driver.find_element_by_tag_name('h1').text
    publisher = driver.find_element_by_class_name('namePlublisher').text
    print(f'\n- Revista: {journal}\n- Publicação de: {publisher}\n')
    articles_list = driver.find_element_by_class_name('articles')
    links = articles_list.find_elements_by_class_name('links')
    for article in links:
        try:
            article_link = article.find_element_by_tag_name('a').get_attribute("href")
            xml_link = article_link.replace('abstract/', '')
            xml_link = re.sub("(\?[a-z]+=[a-z]+$)","?format=xml", xml_link)
            xml_name = xml_link.replace(f'{link}a','')
            alterar = re.sub(r"[(:\(\)<>?/\\|@+)]", "", xml_name)
            full_name = re.sub(r"\s+", "_", alterar)
            full_name = full_name.replace("format=xml",'.xml')
            path_org = os. path. join(diretorio, 'XML')
            path_final = os.path.join(path_org, pasta)
            if not os.path.exists(path_final):
                os.makedirs(path_final)
            out_xml = os.path.join(path_final, full_name)
            if not os.path.exists(out_xml):
                try:
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
        except:
            print('\nsem link')
    if len(error_xml_list)!=0:
        report_erro (path_final, error_xml_list, saveMode)
    if len(error_pdf_list)!=0:    
        report_erro_pdf(pasta, error_pdf_list,saveMode)
