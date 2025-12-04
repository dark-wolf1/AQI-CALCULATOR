import pandas as pd

df = pd.read_csv('aqi.csv')
df.drop(['CO AQI Value',
       'CO AQI Category', 'Ozone AQI Value', 'Ozone AQI Category',
       'NO2 AQI Value', 'NO2 AQI Category', 'PM2.5 AQI Value',
       'PM2.5 AQI Category'], axis = 1, inplace=True)
print(df.columns)
country = pd.get_dummies(df['Country'])
country = list(country.columns)
city  = pd.get_dummies(df['City'])
city = list(city.columns)
category = pd.get_dummies(df['AQI Category'])
category = list(category.columns)


while True:
    print('Main Menu')
    print('1 AQI Values of Countries')
    print('2 AQI Values for Cities')
    print('3 Add New Data')
    print('4 AQI Category')
    print('5 End Program')
    opt = int(input('Enter Option Number: '))
    if opt == 1:
        cn = input('Enter country name: ')
        print(df[df['Country'] == cn])
    if opt == 2:
        ci = input('Enter city name: ')
        print(df[df['City'] == ci])
    if opt == 3:
        cn = input('Enter country name: ')
        ci = input('Enter city name: ')
        val = int(input('Enter AQI Value: '))
        if val<=50:
            cat = 'Good'
        elif val>=51 and val<=100:
            cat = 'Moderate'
        elif val>=101 and val<=300:
            cat = 'Unhealthy'
        elif val>300:
            cat = 'Hazardous'
        data = [cn,ci,val,cat]
        df.loc[len(df)] = data
    if opt == 4:
        cat = input('Enter Category: ')
        print(df[df['AQI Category'] == cat])
    if opt == 5:
        break

