#!/usr/bin/env python
# coding: utf-8

# In[52]:


#importando módulos
import tabula
import math
import pandas as pd
from PyPDF2 import PdfFileReader, PdfFileWriter
reader = PdfFileReader(open("./mao225.pdf", mode='rb' ))
numPages = reader.getNumPages()

print("numero total de paginas", str(numPages))

# df = tabula.read_pdf('mao213.pdf', pages = 1, lattice = True)[1]
df = pd.DataFrame()
for i in range(1, numPages + 1):
    print(i)
    aux = oi(i)
    df = pd.concat([df,aux])
    
df.to_csv('AlunoRelGerado.csv', index=False)
print('ok')


# In[50]:


def oi(num):
    
    #lendo o arquivo pdf, limpando as colunas para coletar a serie e turma
    df = tabula.read_pdf('mao225.pdf', pages = num, lattice = True)[1]
    df.columns = df.columns.str.replace('\r', ',')
    colunas = str(df.head()).split(',')
    turma = colunas[-1][0]
    serie = colunas[5][0]
    
    if(turma == 'X'):
        return

    #parte 2

    df = tabula.read_pdf('mao225.pdf', pages = num, lattice = True)[2]

    abandono = df['ABANDON\rO']
    retido = df['Unnamed: 3']

    df = df.drop(columns=['N°.', 'CÓDIGO\rALUNO', 'CÓDIGO INEP','Unnamed: 0',
                     'Unnamed: 2','Unnamed: 4', 'NECESSIDADE\rESPECIAL', 'COR\r/RAÇA', 'Unnamed: 3', 'ABANDON\rO'])

    df = df.rename(columns={"ALUNO (A)": "Aluno", "DATA\rNASCIMENTO": "Data Nascimento",
                       "Unnamed: 1":"Sexo:"})

    #parte 3

    total_alunos = df['Aluno'].count()
    df = df.dropna(thresh=3) #remove as linhas que tiverem 3 nan
    df = df.fillna('') #nan para vazio

    #parte 4
    df['Turma'] = turma
    df['Serie'] = serie
    df['Situação'] = abandono.fillna('') + retido.fillna('') 

    
    return df


# In[ ]:


# 

