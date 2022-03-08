<p align="left"><img src="img/logo.png" height="256" width="256"/></p>

# Ferramentas Scielo v2 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5168728.svg)](https://doi.org/10.5281/zenodo.5168728) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

>Essa ferramenta é parte dos projetos desenvolvidos pelos membros do [LABHDUFBA](http://labhd.ufba.br/) e tem como objetivo oferecer ferramentas de raspagem, organização e análise de artigos científicos publicados na plataforma [Scielo.br](https://www.scielo.br/).

No ano de 2020, desenvolvemos uma ferramenta para raspagem da base de artigos do Scielo.br. A ferramenta utilizava a biblioteca `BeautifulSoup` para coletar os dados. Entretanto, em 2021 o repositório Scielo.br passou por uma reestruturação completa.

Foi necessário, consequentemente, a reconstrução da ferramenta para lidar com a nova versão do site. Agora, utilizamos o `Selenium` para acessar e raspar os dados do repositório.

Com a `ferramentas_scielo_v2` é possível realizar a raspagem por área do conhecimento ou [por revista (ou uma lista de revistas)](#scielo_rev_v2py). Também é possível optar pelo tipo de raspagem: apenas XML ou XML e PDFs.

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

Exemplo de como executar utilizando o terminal do Linux, após instalar o Python3.8:

1. Acesse o diretório em que o arquivo .py está salvo:
   ```{.sh}
   $ cd user/local
   ```
2. Instale as bibliotecas requeridas:
   ```{.sh}
   $ pip3 install -r requirements.txt
   ```
3. Execute o arquivo usando Python3.8
   ```{.sh}
   $ python3 scielo_v2.py
   ```

### Raspagem por área de conhecimento: `scielo_v2.py`

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

### Raspagem por revista ou por lista de revistas: `scielo_rev_v2.py`

Nesse script é possível raspar uma revista ou uma lista de revistas específicas através de seu nome.

Possui as mesmas características do `scielo_v2.py`, porém a definição da(s) revista(s) a ser(em) raspada(s) é feita através da abreviação do nome da revista conforme URL da revista no site do Scielo.br.

Por exemplo, se vc pretende raspar os arquivos da revista Almanack, acesse a página inicial da revista no repositório e encontre a abreviação de seu título na URL.

```
https://www.scielo.br/j/alm/
```

Nesse caso, o abreviação do nome da revista é `alm`. Esse termo deve ser informado para o programa.

:warning: Atenção

Ambos os scripts criarão diretórios para armazenar os arquivos e dados.

- `scielo/{AAAA-MM-DD}/PDF/{nomeDaRevista}` no caso da raspagem de PDFs;
- `scielo/{AAAA-MM-DD}/XML/{nomeDaRevista}` no caso da raspagem de XMls.

Entretanto, se a pasta com o nome de uma revista já existir no mesmo caminho que o programa está sendo executado, só serão baixados arquivos que ainda não existem.

## Conversão de XML para CSV

Após o download dos arquivos XML é possível utilizar a ferramenta `scielo_xml_to_csv` para converter todos os XML para um arquivo `csv`.

Acesse a pasta `scielo_xml_to_csv` e execute o arquivo `run.py`.

Para mais informações leia o [README.md](scielo_xml_to_csv/README.md) da ferramenta.
