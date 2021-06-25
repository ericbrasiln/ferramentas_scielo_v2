<p align="center"><img src="img/labhd.png" height="256" width="256"/></p>

# scielo_xml_to_csv

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

**Scripts para converter Dataset de XML  das revistas do _Scielo_ (previamente baixado) para CSV.**
  
Esses scripts tem como objetivos analisar, selecionar, organizar e salvar informações de um dataset de arquivos XML de todas as revistas previamente baixados a partir do código [`ferramentas_scielo`](FERRAMENTAS_SCIELO/) em um arquivo CSV.

---

O `run.py` acessa o diretório contendo as pastas de cada revista e analisa cada XML, inserindo os dados em um arquivo CSV salvo com o nome `metadata_{revista}.csv`. 

:warning: _É preciso definir o caminho do diretório com o dataset. E a estrutura desse dataset deve conter diretórios de cada revista (ou edições) com seus arquivos XML a serem analisados._

---

As seguintes informações são inseridas no CSV:

- index,
- file_name: nome do arquivo,
- article_id: identificação do arquivo,
- article_category: categoria do arquivo,
- authors: lista de autores,
- contact_email: e-mail do/a autor/a principal
- authors affiliation: lista de filiações,
- article_title: título do artigo,
- journal_title: título do revista,
- journal_issn: ISSN da revista,
- journal_publisher: instituição da revista,
- pub_date: data da publicação,
- abstract: resumo,
- key_words: lista de palavras-chave,
- issue: edição,
- num: número,
- doi: DOI,
- full_text: texto completo do artigo,
- footnotes: notas de rodapé,
- refs: lista (contendo listas) das referências bibliográficas.

---

Em seguida, com a função `df_final()`, todos os arquivos CSV são unidos em um único dataframe com `Pandas` e salvos em um CSV chamado `metadata_scielo_{yyyy-mm-dd_H-M-S}.csv`.

---

Elementos presentes nesse repositório foram retirados de [Scielo_Journal_Metadata_Downoader](https://github.com/johnsgomez/Scielo_Journal_Metadata_Downoader), criado por [johnsgomez](https://github.com/johnsgomez)

---
## Licença

[MIT Licence](../LICENSE)

2021 [Eric Brasil (IHL/UNILAB, LABHDUFBA)](https://github.com/ericbrasiln), [Gabriel Andrade (UFBA, LABHDUFBA)](https://github.com/gabrielsandrade), [Leonardo Nascimento (UFBA, LABHDUFBA)](https://github.com/leofn)
