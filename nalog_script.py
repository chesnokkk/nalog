import pandas as pd
data = pd.read_excel('nalog.xlsx')
cleaned_df = data.loc[data['Сумма']>0]
nalog=[]
for i in cleaned_df.iloc():
    nalog.append('Skrill' in i['Операция'])
cleaned_df['Налог'] = nalog
result_table = cleaned_df[cleaned_df['Налог']][['Дата транзакции','Операция', 'Сумма', 'Валюта']]
with open('nalog.html','w')as file:
    file.write(result_table.to_html())
