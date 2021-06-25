import pandas as pd 
import os
import time
import glob

def df_final(datasetCSV):
    # Função para unir todos os arquivos CSV e gerar CSV final
    os.chdir(datasetCSV) # Acessa o diretório onde os arquivos CSV foram salvos
    data = time.strftime("%Y-%m-%d_%H%-M%-S") # Define o dia e a hora
    csvs = [] # Lista de arquivos CSV exixtentes
    for f in glob.glob("*.csv"): # Iteração no diretório buscando arquivos que terminem com '.csv'
       csvs.append(pd.read_csv(f)) # Inclusão do CSV na lista
    frame = pd.concat(csvs) # Pandas concatena todos os arquivos CSV
    frame.rename(columns={'Unnamed: 0': 'original_index'}, inplace = True)
    # Criar diretório para CSV final
    csvFinal = os.path.join('metadata_scielo') 
    if not os.path.exists(csvFinal):
      os.makedirs(csvFinal)
    os.chdir(csvFinal) # Acessa o diretório
    # Exportar para CSV
    frame.to_csv( f"metadata_scielo_{data}.csv", index=True, encoding='utf-8-sig')
