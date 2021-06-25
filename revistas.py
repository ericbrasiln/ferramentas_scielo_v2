import time, re
from issue_xml import*
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

def revistas (diretorio, link, link_journal, journal_name, saveMode):
    '''
    função para acessar cada revista.
    '''
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(link_journal)
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
    alterar = re.sub(r"[(,.:\(\)<>?/\\|@+)]", "", journal_name)
    pasta = re.sub(r"\s+", "_", alterar)
    issue_box = driver.find_element_by_id('issueList')
    issue_table = issue_box.find_element_by_tag_name('table')
    issues = issue_table.find_elements_by_tag_name('a')
    for issue in issues:
        issue_link = issue.get_attribute("href")
        print(f'\nLink da edição: {issue_link}')
        get_issue(diretorio, link, issue_link, pasta, saveMode)
