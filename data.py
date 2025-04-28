import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio
import plotly.express as px
import matplotlib.pyplot as plt
pio.renderers.default = 'browser'


'''dataset1=pd.read_csv('covid.csv')
#print(dataset1.shape)
#print(dataset1.size)
#dataset1.info()

dataset2=pd.read_csv('covid_grouped.csv')
#print(dataset2.shape)
#print(dataset2.size)
#dataset2.info()

dataset3=pd.read_csv('coviddeath.csv')
#print(dataset3.shape)
#print(dataset3.size)
#print(dataset3.info())

#print(dataset1.columns)
dataset1.drop(['NewCases','NewDeaths','NewRecovered'],axis=1,inplace=True)	
#print(dataset1.sample(5))

'''
dataset1=pd.read_csv('covid.csv')
dataset1.drop(['NewCases','NewDeaths','NewRecovered'],axis=1,inplace=True)
# Build the table properly
'''fig = go.Figure(data=[go.Table(
    header=dict(values=list(dataset1.columns),
                fill_color='#4d004c',
                font_color='white',
                align='left'),
    cells=dict(values=[dataset1[col].head(15) for col in dataset1.columns],
               fill_color=[['#f2e5ff' if i % 2 == 0 else '#ffffff' for i in range(15)] for _ in dataset1.columns],
               align='left'))
])'''



fig=px.bar(dataset1.head(15), x = 'Country/Region', 
       y = 'TotalCases',color = 'TotalCases', 
       height = 500,hover_data = ['Country/Region', 'Continent'])
fig.show()




