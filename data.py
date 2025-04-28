# COVID-19 Data Analysis and Visualization

import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio
import plotly.express as px
import matplotlib.pyplot as plt
from IPython.display import clear_output
from wordcloud import WordCloud

pio.renderers.default = 'browser'  # 'browser' or 'notebook' or 'vscode'    


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
dataset2=pd.read_csv('covid_grouped.csv')
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

clear_output(wait=True)

'''fig=px.bar(dataset1.head(15), x = 'TotalCases', y = 'Country/Region',
       color = 'TotalTests',orientation='h', height = 500, hover_data = ['Country/Region', 'Continent'])
fig=px.scatter(dataset1.head(25),
               x='Country/Region',
               y='Tests/1M pop',
               title='COVID-19 Cases by Country/Region and Total Cases',
               color='Country/Region',
               size='Tests/1M pop',
               size_max=60,
               hover_data=['Country/Region', 'Continent']
               )

df_US= dataset2.loc[dataset2["Country/Region"]=="US"]


fig=px.choropleth(dataset2,
              locations="iso_alpha",
              color="Confirmed",
              hover_name="Country/Region", 
              color_continuous_scale="RdYlGn",
              projection="natural earth",	
              animation_frame="Date")'''


#fig=px.bar(dataset2, x="WHO Region", y="Confirmed", color="WHO Region", 
       #animation_frame="Date", hover_name="Country/Region")

#fig.show()

dataset3=pd.read_csv('coviddeath.csv')
dataset3.drop(['Flag'],axis=1,inplace=True)
dataset3.groupby(["Condition"]).count()


sentences = dataset3["Condition"].tolist()
sentences_as_a_string = ' '.join(sentences)


# Convert the string into WordCloud
plt.figure(figsize=(20, 20))
plt.imshow(WordCloud().generate(sentences_as_a_string))
plt.axis('off')
plt.title("WordCloud of Conditions for COVID", fontsize=30, color='black')
plt.show()