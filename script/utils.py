import pandas as pd
import openpyxl


def le_dados(arq):

    dir = './data/'
    df = pd.read_excel(dir+arq)
    p = list(df['Peso (kg)'])
    v = list(df['Valor (R$)'])
    
    return p, v