import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('aqi.csv')
df.drop(['CO AQI Value',
       'CO AQI Category', 'Ozone AQI Value', 'Ozone AQI Category',
       'NO2 AQI Value', 'NO2 AQI Category', 'PM2.5 AQI Value',
       'PM2.5 AQI Category'], axis = 1, inplace=True)

country = pd.get_dummies(df['Country'])
country = list(country.columns)
city  = pd.get_dummies(df['City'])
city = list(city.columns)
category = pd.get_dummies(df['AQI Category'])
category = list(category.columns)
num = []
for i in category:
    x = len(df[df['AQI Category'] == i])
    num.append(x)
    

plt.bar(category,num, color = ['green','brown','yellow','orange','blue','red'], linewidth = 1,edgecolor = 'black')
plt.xlabel('AQI Categories')
plt.ylabel('No of Cities')
plt.title('AQI Categories V/S No of Cities')
plt.show()

inp = input('Enter country name: ')
l_city = df['City'][df['Country'] == inp].head()
l_value = df['AQI Value'][df['Country'] == inp].head()
plt.bar(l_city,l_value, color = 'purple')
plt.xlabel('City Name')
plt.ylabel('AQI Value')
plt.title('AQI Values of Cities in a Country')
plt.show()