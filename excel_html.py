import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import re


df = pd.read_excel(r'Visão Geral Iniciativas_v2.xlsm', sheet_name='ACOMPANHAMENTO GERAL', index_col=0)

df.style.set_properties(**{'text-align': 'center'})

def style_line(s):
    '''Rendering odd and even rows with different color'''
    print(s)
    return ['color: #D4E6F1' if i else 'color: #85C1E9' for i in range(len(s))]
# print(style_line)



df = df.fillna('')
df.style.apply(style_line, subset = 'Pendências TI').render()

df = df.replace('\n','|', regex=True)

html = df.to_html(classes=["table-bordered", "table-striped", "table-hover"], col_space=180)

qtde_check = len(re.findall('ü',html))
qtde_progress = len(re.findall('Ü',html))
qtde_late = len(re.findall('Â',html))


html = str(html).replace('|','<br>')
n_ini = 1
for i in range(1,qtde_check):
    ini = html.find('ü',n_ini)
    # print(ini)
    html = html[:ini-1] + ' style="color: blue"' + html[ini-1:]
    n_ini = ini+22

n_ini = 1
for i in range(1,qtde_progress):
    ini = html.find('Ü',n_ini)
    # print(ini)
    html = html[:ini-1] + ' style="color: green"' + html[ini-1:]
    n_ini = ini+23

n_ini = 1
for i in range(1,qtde_late):
    ini = html.find('Â',n_ini)
    # print(ini)
    html = html[:ini-1] + ' style="color: red"' + html[ini-1:]
    n_ini = ini+22

html = re.sub('ü',r'<i class="fas fa-check" style="color:blue"></i>', html)
html = re.sub('Ü',r'<i class="fas fa-arrow-circle-right" style="color:green"></i>', html)
html = re.sub('â',r'<i class="far fa-clock" style="color:red"></i>', html,flags=re.IGNORECASE)


head = '''<!DOCTYPE html>
<html lang="pt">
<head>    
    <meta charset="UTF-8">    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title>Home</title>
</head>
<body>
<style>
body {margin: 5px;}
table {text-align: center;}
table thead th {text-align: center;}
</style>
'''


text_file = open('teste.html', 'w', encoding="utf-8")
text_file.write(head)
text_file.write('\n')
text_file.write(html)
text_file.close()