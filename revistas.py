import time, re
from issue_xml import*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def revistas (diretorio, link, link_journal, journal_name, saveMode):
    '''
    função para acessar cada revista.
    '''
    firefox_options = Options()
    firefox_options.add_argument('-lang=pt-BR')
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--start-maximized")
    s=Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=s, options=firefox_options)
    driver.get(link_journal)
    #Botão de aceitar cookies
    try:
        cookies = driver.find_element(By.CLASS_NAME,'alert-cookie-notification')
        #Clicando para fechar o aviso
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[7]/a')
            )).click()
    except:
        pass
    time.sleep(1)
    alterar = re.sub(r"[(,.:\(\)<>?/\\|@+)]", "", journal_name)
    pasta = re.sub(r"\s+", "_", alterar)
    issue_box = driver.find_element(By.ID,'issueList')
    issue_table = issue_box.find_element(By.TAG_NAME,'table')
    issues = issue_table.find_elements(By.TAG_NAME,'a')
    for issue in issues:
        issue_link = issue.get_attribute("href")
        print(f'\nLink da edição: {issue_link}')
        get_issue(diretorio, link, issue_link, pasta, saveMode)
