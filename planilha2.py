import os, requests
import os, openpyxl

url = requests.get('https://www.seade.gov.br/coronavirus/')

print("Status:",url.status_code)

print("Header:",url.headers,"\n")

planilha = openpyxl.Workbook()



page = planilha['Doses']
page.title = 'Dados Covid 19'

page.append(['LOCAL', 'DOSES'])
page.append(['MUNDO', '9,98 bi'])
page.append(['BRASIL', '357 mi'])
page.append(['SÃO PAULO', '91,5 mi'])


planilha.save('planilha2.xlsx')

os.system("pause")