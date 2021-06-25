import os, time
from reports import report_scrape_rev
from revistas import revistas

timestr = time.strftime("%Y-%m-%d")
saveMode = ''
def main():
    global saveMode
    while (saveMode != 1 and saveMode != 2):
        revList = list()
        print('-=- Definição da(s) revista(s) -=-\n')
        while True:
            revList.append(str(input('Digite a abreviação da revista que deseja raspar: ')))
            resp = str(input('Deseja inserir outra? [S/N] '))
            if resp in 'Nn':
                print('-='*50)
                break
        saveMode = int(input('-=-Definição do tipo de raspagem-=-\n'
                     '1- Salvar os XMLs;\n'
                     '2- Salvar os XMLs e baixar os PDFs.\n'
                     'Tipo de Raspagem (1 ou 2): '))
        diretorio = os.path.join('scielo',timestr)
        if not os.path.exists(diretorio):
            #Se a pasta ainda não existir, cria a pasta
            os.makedirs(diretorio)
        report_scrape_rev(diretorio, timestr, revList, saveMode)
        for revista in revList:
            link = f'https://www.scielo.br/j/{revista}/'
            link_final = link+'grid'
            revistas (diretorio, link, link_final, revista, saveMode)

if __name__ == "__main__":
    main()
