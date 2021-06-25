import os
from datetime import datetime

now = datetime.now()
data_hora = now.strftime("%Y-%m-%d_%H-%M-%S")

def report_scrape(diretorio, time, theme, saveMode):
    '''
    Função para criar relatório geral da raspagem
    '''
    if saveMode == 1:
        tipo = 'Apenas XLM'
    else:
        tipo = 'XML e Download de PDF'
    if theme == '1':
        theme = 'Ciências Agrárias'
    elif theme == '2':
        theme = 'Ciências Biológicas'
    elif theme == '3':
        theme = 'Ciências da Saúde'
    elif theme == '4':
        theme = 'Ciêncas Exatas e da Terra'
    elif theme == '5':
        theme = 'Ciências Humanas'
    elif theme == '6':
        theme = 'Ciências Sociais Aplicadas'
    elif theme == '7':
        theme = 'Engenharias'
    elif theme == '8':
        theme = 'Linguística, Letras e Artes'
    out_relatório = os.path.join(diretorio, 'RELATÓRIO_GERAL')
    #Criando relatório
    relatório = open(f'{out_relatório}_{time}.txt', 'w')
    #Inserindo dados no relatório
    relatório.write(
        f'=-=-=-=-=-Relatório da raspagem-=-=-=-=-=\n'
        f'- Data e hora: {time};\n'
        f'- Área Temática: {theme};\n'
        f'- Tipo de raspagem: {tipo}\n'
        )
    relatório.close

def report_scrape_rev(diretorio, time, revList, saveMode):
    '''
    Função para criar relatório de raspagem de lista de revistas
    '''
    if saveMode == 1:
        tipo = 'Apenas XLM'
    else:
        tipo = 'XML e Download de PDF'
    out_relatório = os.path.join(diretorio, 'RELATÓRIO_GERAL_REVISTAS')
    #Criando relatório
    relatório = open(f'{out_relatório}_{time}.txt', 'w')
    #Inserindo dados no relatório
    relatório.write(
        f'=-=-=-=-=-Relatório da raspagem-=-=-=-=-=\n'
        f'- Data e hora: {time};\n'
        f'- Lista de revistas: {revList};\n'
        f'- Tipo de raspagem: {tipo}\n'
        )
    relatório.close    

def report_erro (diretorio,error_list, saveMode):
    '''
    Função para criar relatório com erros ao baixar o xml.
    '''
    if saveMode == 1:
        tipo = 'Apenas XLM'
    else:
        tipo = 'XML e Download de PDF'
    #Criando pasta para salvar relatórios
    report_path = diretorio
    out_relatório = os.path.join(report_path, 'RELATÓRIO_ERRO')
    #Criando relatório
    relatório = open(f'{out_relatório}_{data_hora}.txt', 'w')
    #Inserindo dados no relatório
    relatório.write(
        f'=-=-=-=-=-Relatório de erro-=-=-=-=-=\n'
        f'- Data e hora: {data_hora};\n'
        f'- Tipo de raspagem: {tipo};\n'
        f'- Link do xml que apresentou erro e não foi baixado: {error_list}\n'
        )
    relatório.close

def report_erro_pdf (diretorio, error_pdf_list, saveMode):
    '''
    Função para criar relatório com erros ao baixar PDF.
    '''
    if saveMode == 1:
        tipo = 'Apenas XLM'
    else:
        tipo = 'XML e Download de PDF'
    #Criando pasta para salvar relatórios
    current_dir = os.curdir
    report_path = os.path.join(current_dir, diretorio)
    out_relatório = os.path.join(report_path, 'RELATÓRIO_ERRO')
    #Criando relatório
    relatório = open(f'{out_relatório}_{data_hora}.txt', 'w')
    #Inserindo dados no relatório
    relatório.write(
        f'=-=-=-=-=-Relatório de erro-=-=-=-=-=\n'
        f'- Data e hora: {data_hora};\n'
        f'- Tipo de raspagem: {tipo};\n'
        f'- Link do pdf que apresentou erro e não foi baixado: {error_pdf_list}\n'
        )
    relatório.close
