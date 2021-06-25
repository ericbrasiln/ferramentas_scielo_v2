#Funções para extrair informações do xml     
def find_article_category(soup):
    try:
        article_category = soup.find("subject")
        return(article_category.string)
    except: # Se não encontrar, insere "None"
        article_category = 'None'
        return(article_category)

def find_article_id(soup):
    try: # Tenta encontrar no XML
        article_id = soup.front.find("article-id")
        return(article_id.string)
    except: # Se não encontrar, insere "None"
        article_id = 'None'
        return(article_id)
    
def find_article_title(soup):
    '''
    Encontrar o título do artigo 
    '''
    try:
        article_group = soup.front.find("title-group")
        article_title = article_group.find("article-title")
        return(article_title.text)
    except:
        article_title = 'None'
        return(article_title)
    
def find_authors(soup):
    try:
        authors_lastnames = soup.front.find_all(["surname"])
        authors_names = soup.front.find_all(["given-names"])
        authors = [] # Lista para armazenar nomes e sobrenomes dos/as autores/as
        for author in range(len(authors_lastnames)): # Iteração juntando nomes e sobrenomes
            authors.append(authors_names[author].string + " " + authors_lastnames[author].string)
        return(", ".join(authors)) # Separa diferentes autores por ','
    except:
        authors = 'None'
        return(authors)
def find_email(soup):
    try:
        email = soup.find("email")
        return(email.string)
    except:
        email = "None"
        return(email)

def find_authors_aff(soup):
    try:
        authors_inst = soup.front.find_all(["institution"])
        authors_country = soup.front.find_all(["country"])
        authors_aff = [] # Lista para armazenar filiações institucionais dos/as autores/as
        for aff in range(len(authors_country)): # Iteração juntando instituição com país
            authors_aff.append(authors_inst[aff].string + " " + authors_country[aff].string)
        return(", ".join(authors_aff)) # Separa diferentes instituições por ','
    except:
        authors_aff = 'None'
        return(authors_aff)
  
def find_pub_date(soup):
    try:
        month = soup.front.find("pub-date").contents[3].string
        year = soup.front.find("pub-date").contents[5].string
        date = [year,month] # Cria lista com ano e mês da públicação
        return('-'.join(date)) # Separa ano e mês com "-"
    except:
        date = "None"
        return(date)
    
def find_issue(soup): #issue
    try:
        issue = soup.front.find("issue")
        return(issue.string)
    except:
        issue = "None"
        return(issue)

def find_num(soup):
    try:
        num = soup.front.find("numero")
        return(num.string)
    except:
        num = "None"
        return(num)

def find_doi(soup):
    try:
        doi = soup.front.find("article-id",attrs={'pub-id-type': 'doi'})
        return(doi.string)
    except:
        doi = 'None'
        return(doi)

def find_journal_title(soup):
    try:
        journal_title = soup.front.find("journal-title")
        return(journal_title.string)
    except:
        journal_title = "None"
        return(journal_title)
    
def find_journal_issn(soup):
    try:
        journal_issn = soup.front.find("issn")
        return(journal_issn.string)
    except:
        journal_issn = "None"
        return(journal_issn)

def find_journal_publisher(soup):
    try:
        journal_publisher = soup.front.find("publisher-name")
        return(journal_publisher.string)
    except:
        journal_publisher = "None"
        return(journal_publisher)
    
def find_key_words(soup):
    try:
        key_words = soup.front.find("kwd-group") # Encontra o primeiro conjunto de 
        # palavras-chave (idioma principal)
        kwd = key_words.find_all("kwd")
        kwd = [word.string for word in kwd] # Criação de uma lista com as palavras-chave, atrvés de uma iteração, que tb as transforma em string
        return ", ".join(kwd) # Separa cada palavra-chave com ", "
    except:
        kwd = "None"
        return(kwd)
    
def find_abstract(soup):
    try:
        abstract = soup.front.find("abstract") # Encontra o primeiro resumo (idioma principal)
        abstract_text = abstract.find("p")
        return(abstract_text.text)
    except:
        abstract_text = "None"
        return(abstract_text)

def get_text(soup):
    try:
        body = soup.find("body")
        return(body.text)
    except:
        body = "None"
        return(body)

def get_refs(soup):
    try:
        back = soup.find('back')
        refList = back.find('ref-list')
        refsCitations = refList.find_all('ref')
        listaRefFinal = []
        for c in refsCitations:
            ref_complete = c.find('mixed-citation')
            listaRefFinal.append(ref_complete.text)
        return(listaRefFinal)
    except:
        listaRefFinal = "Not Found"
        return(listaRefFinal)

def get_fn(soup):
    try:
        back = soup.find('back')
        fn_group = back.find('fn-group')
        listaFootnotes = []
        notes = fn_group.find_all('fn')
        for fn in notes:
            label = fn.find('label').text
            text = fn.find('p').text
            note = f'n{label} - {text}'
            listaFootnotes.append(note)
        return(listaFootnotes)
    except:
        listaFootnotes = "Not found"
        return(listaFootnotes)
        