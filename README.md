# COVID-19 Data Analysis and Visualization

This project is focused on analyzing and visualizing COVID-19 data using Python. It utilizes popular libraries like **Pandas**, **Plotly**, **Matplotlib**, and **WordCloud** to explore, analyze, and visualize important trends in COVID-19 statistics across various countries and regions.

## Project Overview

The main objective of this project is to:
- Analyze **COVID-19 case** data (cases, deaths, and recoveries) across multiple countries.
- Visualize the data using interactive plots and maps.
- Create a **WordCloud visualization** to display the most common conditions associated with COVID-19 deaths.

### Datasets Used
The project uses three datasets:
1. **covid.csv** – Contains global data on COVID-19 cases, deaths, and tests.
2. **covid_grouped.csv** – Contains grouped data by country, including confirmed cases and other statistics.
3. **coviddeath.csv** – Contains information about the conditions associated with COVID-19-related deaths.

# Code Walkthrough
### 1. Data Loading
The project starts by loading three CSV files:

covid.csv

covid_grouped.csv

coviddeath.csv

### 2. Data Cleaning
covid.csv: The columns NewCases, NewDeaths, and NewRecovered are removed to focus on more relevant statistics.

coviddeath.csv: The Flag column is dropped to focus on the conditions related to COVID-19 deaths.

### 3. Data Visualizations
#### A. Bar Chart of Total COVID-19 Cases
A bar chart is created to visualize the total number of cases per country, with a horizontal layout, categorized by the number of tests conducted.

#### B. Scatter Plot of Tests vs. Total Cases
A scatter plot visualizes the relationship between the number of tests conducted per million people and the total cases per country.

#### C. Choropleth Map of COVID-19 Confirmed Cases
A choropleth map is generated to show COVID-19 cases by country. This map is animated over time to visualize how the pandemic spread across the globe.

#### D. WordCloud of Conditions for COVID-19 Deaths
A WordCloud is created from the conditions associated with COVID-19 deaths. The most frequent conditions are displayed in a cloud of words.

## Example Output
Here are some sample visualizations you can expect when running the code:

Bar Chart of Total COVID-19 Cases by Country

Scatter Plot of Tests vs. Total Cases

Choropleth Map of COVID-19 Confirmed Cases

Word Cloud of Conditions for COVID-19 Deaths


![Screenshot 2025-04-28 201132](https://github.com/user-attachments/assets/b893d502-4839-47f8-91f0-4fab2aae2938)
![Screenshot 2025-04-28 201034](https://github.com/user-attachments/assets/504843cb-0bec-43de-bc19-aab786277174)
![Screenshot 2025-04-28 195604](https://github.com/user-attachments/assets/02ba454a-4ed3-4271-95eb-14e74446ecb1)
![Screenshot 2025-04-28 191236](https://github.com/user-attachments/assets/671886f0-510e-478e-8670-245642e8366f)
![Screenshot 2025-04-28 185043](https://github.com/user-attachments/assets/7436f0d8-51f7-40a9-b149-a7eac75a7272)
![Screenshot 2025-04-28 184946](https://github.com/user-attachments/assets/ce42e906-bc46-430d-853b-439e91f6743b)
