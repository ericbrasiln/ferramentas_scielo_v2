from xml.etree import ElementTree as ET

def referenciasXml(entry, refs):
    try:
        tree = ET.parse(entry) # Analisa o arquivo XML
        root = tree.getroot()
        articleRefs = root.find('back')
        refList = articleRefs.find('ref-list')
        refsCitations = refList.findall('ref')
        print(len(refsCitations))
        listaRefFinal = []
        for c in refsCitations:
            ref_complete = c.find('mixed-citation')
            listaRef = []
            # Tipo de referência
            typeRef = c.find('[@citation-type]').attrib
            typeRef = str(typeRef)
            typeRef = typeRef.replace("{'citation-type': '", "")
            typeRef = typeRef.replace("'}", "")
            if c.find('person-group/[@person-group-type="editor"]') == None:
                listaRef.append(typeRef)
            else:
                typeRef = 'Book Section'
                listaRef.append(typeRef)
            # autore/es
            refAutores = c.find('person-group/[@person-group-type="author"]')
            try:
                refAutor = refAutores.findall('name')
                listaAuthRef = []
                nomes = {}
                for a in refAutor:
                    surname = a.find('surname')
                    surname = surname.text
                    givenName = a.find('given-names')
                    givenName = givenName.text
                    author = (givenName + ' ' + surname)
                    listaAuthRef.append(author)
                listaAuthRef = ', '.join(listaAuthRef)
                listaRef.append(listaAuthRef)
            except:
                pass
            # Título do artigo
            articleTitle = c.find('article-title')
            if articleTitle != None:
                articleTitle = articleTitle.text
                listaRef.append(articleTitle)
            # Editores/orgs
            refEditors = c.find('person-group/[@person-group-type="editor"]')
            if refEditors !=None:
                editor = refEditors.findall('name')
                listaEdRef = []
                nomeEd = {}
                for e in editor:
                    surname = e.find('surname')
                    surname = surname.text
                    givenName = e.find('given-names')
                    givenName = givenName.text
                    ed = ('org(s) '+ givenName + ' ' + surname)
                    listaEdRef.append(ed)
                listaEdRef = ', '.join(listaEdRef)
                listaRef.append(listaEdRef)
            # Título do livro ou Revista
            refTitle = c.find('source')
            if refTitle != None:
                refTitle = refTitle.text
                listaRef.append(refTitle)
            refAno = c.find('year')
            if refAno != None:
                refAno = refAno.text
                listaRef.append(refAno)
            refVol = c.find('volume')
            if refVol != None:
                refVol = refVol.text
                refVol = 'v. '+refVol
                listaRef.append(refVol)
            refNum = c.find('numero')
            if refNum != None:
                refNum = refNum.text
                refNum ='n. '+refNum
                listaRef.append(refNum)
            refIssue = c.find('issue')
            if refIssue != None:
                refIssue = refIssue.text
                refIssue = 'ed. '+refIssue
                listaRef.append(refIssue)
            refPages = c.find('page-range')
            if refPages != None:
                refPages = refPages.text
                refPages = 'pp. '+refPages
                listaRef.append(refPages)
            refLoc = c.find('publisher-loc')
            if refLoc !=None:
                refLoc = refLoc.text
                listaRef.append(refLoc)
            refPub = c.find('publisher-name')
            if refPub != None:
                refPub= refPub.text
                listaRef.append(refPub)
            listaRefFinal.append(listaRef)
    except:
        listaRefFinal = "None"
    refs.append(listaRefFinal)
