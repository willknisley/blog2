import urllib.request
import json
import time
import pandas as pd

"""with open("client_id.txt", "r") as id_file:
    client_id = id_file.read().strip()

with open("client_secret.txt", "r") as secret_file:
    client_secret = secret_file.read().strip()

try:
    url = f'https://data.api.xweather.com/conditions/salt%20lake%20city,%20ut?format=json&plimit=1&filter=1min&client_id={client_id}&client_secret={client_secret}'
    with urllib.request.urlopen(url) as request:
        response = request.read()
        data = json.loads(response)
    if data.get('success'):
        print(data)
    else:
        print("An error occurred: %s" % (data.get('error', {}).get('description', 'Unknown error')))

except urllib.error.HTTPError as e:
    if e.code == 401:
        print("Unauthorized: Please check your client ID and client secret.")
    else:
        print(f"HTTP Error {e.code}: {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")"""

weather_data = []

with open("client_id.txt", "r") as id_file:
    client_id = id_file.read().strip()

with open("client_secret.txt", "r") as secret_file:
    client_secret = secret_file.read().strip()

cities = [
    "salt lake city, ut", "denver, co", "boise, id", "spokane, wa", "reno, nv", 
    "phoenix, az", "las vegas, nv", "los angeles, ca", "san francisco, ca", 
    "seattle, wa", "portland, or", "sacramento, ca", "fresno, ca", "tucson, az", 
    "albuquerque, nm", "cheyenne, wy", "helena, mt", "billings, mt", "missoula, mt", 
    "bend, or", "medford, or", "bakersfield, ca", "stockton, ca", "riverside, ca", 
    "pueblo, co", "elko, nv", "flagstaff, az", "great falls, mt", "idaho falls, id"
]

weather_keywords = ["rain", "snow", "drizzle", "thunder", "storm", "cloudy", "windy"]

# Collect data for each city
for city in cities:
    # Encode city name for URL
    city_encoded = urllib.parse.quote(city)
    url = f'https://data.api.xweather.com/conditions/{city_encoded}?format=json&plimit=200&filter=1min&client_id={client_id}&client_secret={client_secret}'
    
    try:
        with urllib.request.urlopen(url) as request:
            response = request.read()
            data = json.loads(response)

            if data.get('success'):
                for period in data['response'][0]['periods']:
                    # Check if the weather description includes any keywords
                    weather_description = period.get("weather", "").lower()
                    if any(keyword in weather_description for keyword in weather_keywords):
                        # Collect features for each relevant observation
                        record = {
                            "city": city,
                            "temperature": period.get("tempF"),
                            "feels_like": period.get("feelslikeF"),
                            "humidity": period.get("humidity"),
                            "wind_speed": period.get("windSpeedMPH"),
                            "weather": weather_description,
                            "sky": period.get("sky")
                        }
                        weather_data.append(record)

    except urllib.error.HTTPError as e:
        print(f"Failed to retrieve data for {city}: HTTP Error {e.code}")
    except Exception as e:
        print(f"An error occurred for {city}: {e}")

    # Pause between requests to avoid hitting rate limits
    #time.sleep(1)

df = pd.DataFrame(weather_data)

# Display the DataFrame
print(df)

df.to_csv('weather_data.csv', index=False)