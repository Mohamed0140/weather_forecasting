import requests
API_KEY = "5e2f73996355d9b3dc825cf2567e1303"

def get_api(place, forcast_day):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    ne_values = 8 * forcast_day
    filtered_data = filtered_data[:ne_values]
    return filtered_data


