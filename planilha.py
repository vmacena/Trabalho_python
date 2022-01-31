import os, requests
import os, openpyxl

url = requests.get('https://www.seade.gov.br/coronavirus/')

print("Status:",url.status_code)

print("Header:",url.headers,"\n")

planilha = openpyxl.Workbook()



page = planilha['planilha2']
page.title = 'Dados Covid 19'

page.append(['LOCAL', 'CASOS', 'VARIAÇÃO DIÁRIA'])
page.append(['MUNDO', '362.510.675', '1%'])
page.append(['BRASIL', '24.535.884', '1%'])
page.append(['SÃO PAULO', '4.609.121', '0%'])


planilha.save('planilha.xlsx')

os.system("pause")