import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('weather_data.csv')

city_climate = df[['city', 'temperature', 'feels_like', 'humidity']]

plt.figure(figsize=(12, 6))
city_climate_melted = pd.melt(city_climate, id_vars=['city'], var_name='Metric', value_name='Value')

sns.barplot(data=city_climate_melted, x='city', y='Value', hue='Metric', palette='viridis')

plt.xticks(rotation=45)
plt.title('Comparison of Temperature, Feels-Like, and Humidity Across Cities')
plt.xlabel('City')
plt.ylabel('Value')
plt.tight_layout()

plt.savefig('san_francisco_climate_comparison.png')
plt.show()


plt.figure(figsize=(10, 6))

sns.barplot(x='city', y='wind_speed', data=df, palette='coolwarm', hue='temperature')

plt.title('Wind Speed vs Temperature by City')
plt.xlabel('City')
plt.ylabel('Wind Speed (MPH)')
plt.xticks(rotation=45)

plt.legend(title='Temperature (°F)', loc='upper left')

plt.tight_layout()

plt.show()

plt.figure(figsize=(10, 6))

sns.barplot(x='city', y='sky', data=df, palette='coolwarm', hue='temperature')

plt.title('Cloud Coverage vs Temperature by City')
plt.xlabel('City')
plt.ylabel('Cloud Coverage (%)')
plt.xticks(rotation=45)

plt.legend(title='Temperature (°F)', loc='upper left')

plt.tight_layout()

plt.show()