from revistas import revistas
from reports import report_scrape
import time, os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

timestr = time.strftime("%Y-%m-%d")
saveMode = ''
def main():
    global saveMode
    while (saveMode != 1 and saveMode != 2):
        url = 'https://www.scielo.br//journals/thematic?status=current'
        # Definição da área do conhecimento para raspagem
        print('-=-Definição da área temática-=-\n')
        area = str(input(
                    '- Opções:\n'
                    '1- Ciências Agrárias\n'
                    '2- Ciências Biológicas\n'
                    '3- Ciências da Saúde\n'
                    '4- Ciências Exatas e da Terra\n'
                    '5- Ciências Humanas\n'
                    '6- Ciências Sociais Aplicadas\n'
                    '7- Engenharias\n'
                    '8- Linguística, Letras e Artes\n'
                    'Digite o número correspondente à área temática que deseja raspar: \n'))
        print('-='*50)
        saveMode = int(input('-=-Definição do tipo de raspagem-=-\n'
                             '1- Salvar os XMLs;\n'
                             '2- Salvar os XMLs e baixar os PDFs.\n'
                             'Tipo de Raspagem (1 ou 2): '))
        diretorio = os.path.join('scielo',timestr)
        if not os.path.exists(diretorio):
            #Se a pasta ainda não existir, cria a pasta
            os.makedirs(diretorio)
        # Definição das opções do driver
        firefox_options = Options()
        firefox_options.add_argument('-lang=pt-BR')
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--start-maximized")
        s=Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s, options=firefox_options)
        driver.get(url)
        #botão de aceitar cookies
        try:
            cookies = driver.find_element(By.CLASS_NAME,'alert-cookie-notification')
            #Clicando para fechar o aviso
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[6]/a[2]')
                )).click()
        except:
            pass
        journal_table = driver.find_element(By.ID,'journals_table_body')
        tematica = journal_table.find_element(By.ID,f"heading-{area}")
        print(f'\n-=-{tematica.text}-=-')
        btn = tematica.find_element(By.TAG_NAME,'a').click()
        time.sleep(1)
        area_box = driver.find_element(By.ID,f'collapseContent-{area}')
        journal_list = area_box.find_elements(By.CLASS_NAME,'collectionLink ')
        report_scrape(diretorio, timestr, area, saveMode)
        for journal in journal_list:
            link = journal.get_attribute("href")
            link_final = link+'grid'
            #Função para acessar o grid
            name = journal.find_element(By.CLASS_NAME,"journalTitle").text
            revistas(diretorio, link, link_final, name, saveMode)
        print('fim da raspagem')

if __name__ == "__main__":
    main()
