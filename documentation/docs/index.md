<p align="left"><img src="img/logo.png" height="256" width="256"/></p>

# Ferramentas Scielo v2 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5168728.svg)](https://doi.org/10.5281/zenodo.5168728) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

No ano de 2020, desenvolvemos uma ferramenta para raspagem da base de artigos do Scielo.br. A ferramenta, escrita em Python, utilizava a biblioteca `BeautifulSoup` para coletar os dados. Entretanto, em 2021 o repositório Scielo.br passou por uma reestruturação completa.

Foi necessário, consequentemente, a reconstrução da ferramenta para lidar com a nova versão do site. Agora, utilizamos o `Selenium` para acessar e raspar os dados do repositório.

Com a `ferramentas_scielo_v2` é possível realizar a raspagem [por área do conhecimento](https://labhdufba.github.io/ferramentas_scielo_v2/#raspagem-por-area-de-conhecimento) ou [por revista (ou uma lista de revistas)](https://labhdufba.github.io/ferramentas_scielo_v2/#raspagem-por-revista-ou-por-lista-de-revistas). Também é possível optar pelo tipo de raspagem: apenas XML ou XML e PDFs.

Também disponibilizamos uma ferramenta para converter os XMLs para CSV, com o script `scielo_xml_to_csv/run.py`.

## Instalação

Para executar a ferramenta é preciso clonar ou fazer download do repositório para sua máquina. Antes de executar os scripts, é preciso preparar seu computador, como mostramos abaixo.

A ferramentas desse projeto foram escritas em [Python 3.8](https://www.python.org/). Portanto, para executar o arquivo .py é preciso instalar o Python3 em seu computador.

[Clique aqui](https://python.org.br/instalacao-windows/) para acessar um tutorial de instalação do Python no Windows, [clique aqui](https://python.org.br/instalacao-linux/) para Linux e [clique aqui](https://python.org.br/instalacao-mac/)
para Mac.

Após a instalação do Python é preciso instalar as bibliotecas necessárias para a ferramenta ser executada. Para isso, basta executar o comando `pip install -r requirements.txt` no terminal, a partir da pasta onde está o arquivo.  Para saber mais sobre instalação de bibliotecas com pip, veja essa lição do [Programming Historian](https://programminghistorian.org/pt/licoes/instalacao-modulos-python-pip).

1. Acesse o diretório em que o arquivo `requirements.txt` está salvo:
   ```{.sh .bash}
   $ cd <caminho para a pasta>
   ```
2. Instale as bibliotecas requeridas com o seguinte comando:
   ```{.python}
   pip install -r requirements.txt
   ```

Agora é possível executar a ferramenta direto do prompt de comando do Windows ou pelo terminal do Linux, ou utilizar as diversas [IDE](https://pt.wikipedia.org/wiki/Ambiente_de_desenvolvimento_integrado) disponíveis.

## Utilização

Na pasta da ferramenta existem dois arquivos python que permitem a execução de opções distintas de raspagem. O primeiro, `scielo_v2.py`, permite a raspagem de todas as revistas de uma determinada área do conhecimento. O segundo, `scielo_rev_v2.py`, permite a raspagem por revista ou lista de revistas específicas.

### Raspagem por área de conhecimento

Esse script permite ao usuário selecionar qual assunto pretende raspar de acordo com a categorização estabelecida pela plataforma [Scielo.br](https://www.scielo.br/journals/thematic?status=current). 

Para isso é preciso executar o seguinte comando, do interior da pasta onde o arquivo está localizado:

```{.sh}
python scielo_v2.py
```
A seguinte mensagem será exibida:

```{.python}
-=-Definição da área temática-=-

- Opções:
1- Ciências Agrárias
2- Ciências Biológicas
3- Ciências da Saúde
4- Ciências Exatas e da Terra
5- Ciências Humanas
6- Ciências Sociais Aplicadas
7- Engenharias
8- Linguística, Letras e Artes
Digite o número correspondente à área temática que deseja raspar: 
```
Após a definição do assunto, é preciso definir o tipo de raspagem: 

1. Realizar a raspagem de todos os arquivos XML de todas as edições de todas as revistas da área selecionada: opção `1`;
2. Realizar a raspagem de todos os arquivos XML e PDF de todas as edições de todas as revistas da área selecionada: opção `2`.
   
:warning: Devido ao volume de dados, contando dezenas de milhares de artigos, o download de todos os arquivos PDF demandará  muito tempo e uso intenso de sua máquina.

    
:warning: Os arquivos XML possuem todos os metadados dos artigos, incluindo o texto completo e as referências bibliográficas.

### Raspagem por revista ou por lista de revistas

Nesse script é possível raspar uma revista ou uma lista de revistas específicas através de seu nome.

Possui as mesmas características do `scielo_v2.py`, porém a definição da(s) revista(s) a ser(em) raspada(s) é feita através da abreviação do nome da revista conforme URL da revista no site do Scielo.br.

Por exemplo, se vc pretende raspar os arquivos da revista Almanack, acesse a página inicial da revista no repositório e encontre a abreviação de seu título na URL.

```{.html}
https://www.scielo.br/j/alm/
```

Nesse caso, o abreviação do nome da revista é `alm`. Esse termo deve ser informado para o programa.

```{.sh}
-=- Definição da(s) revista(s) -=-

Digite a abreviação da revista que deseja raspar: alm
Deseja inserir outra? [S/N]
```

:warning: Atenção

Ambos os scripts criarão diretórios para armazenar os arquivos e dados.

- `scielo/{AAAA-MM-DD}/PDF/{nomeDaRevista}` no caso da raspagem de PDFs;
- `scielo/{AAAA-MM-DD}/XML/{nomeDaRevista}` no caso da raspagem de XMls.

Entretanto, se a pasta com o nome de uma revista já existir no mesmo caminho que o programa está sendo executado, só serão baixados arquivos que ainda não existem.

## Conversão de XML para CSV

Após o download dos arquivos XML é possível utilizar a ferramenta `scielo_xml_to_csv` para converter todos os XML para um arquivo `csv`.

Acesse a pasta `scielo_xml_to_csv` e execute o arquivo `run.py`.

Esses scripts têm como objetivos analisar, selecionar, organizar e salvar informações de um dataset de arquivos XML de todas as revistas previamente baixados em um arquivo CSV.

O `run.py` acessa o diretório contendo as pastas de cada revista e analisa cada XML, inserindo os dados em um arquivo CSV salvo com o nome `metadata_{revista}.csv`. 

:warning: _É preciso definir o caminho do diretório com o dataset. E a estrutura desse dataset deve conter diretórios de cada revista (ou edições) com seus arquivos XML a serem analisados._

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

Em seguida, com a função `df_final()`, todos os arquivos CSV são unidos em um único *dataframe* com `Pandas` e salvos em um CSV chamado `metadata_scielo_{yyyy-mm-dd_H-M-S}.csv`.

---

Elementos presentes nesse repositório foram retirados de [Scielo_Journal_Metadata_Downoader](https://github.com/johnsgomez/Scielo_Journal_Metadata_Downoader), criado por [johnsgomez](https://github.com/johnsgomez)
