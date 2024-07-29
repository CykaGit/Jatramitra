import requests, json
# from pprint import pprint

# open weather api

API_KEY = "8acf4a798c7f6230ff57342319c2945a"


def city(data):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    response = requests.get(base_url + "appid=" + API_KEY + "&q=" + data)
    x = response.json()
    print(x)
    temp = int(x["main"]["temp"] - 273)
    feels = int(x["main"]["feels_like"] - 273)
    humid = int(x["main"]["humidity"])
    desc = x["weather"][0]["description"]
    wind = x["wind"]["speed"]
    arr = [temp, feels, humid, desc, wind]
    print(arr)
    return arr


if __name__ == "__main__":
    prompt = input("Enter City:")
    result = city(prompt)

    # print("Temp:", result["main"]["temp"] - 273)
    # print("Feels Like:", result["main"]["feels_like"])
    # print("Humidity:", result["main"]["humidity"])
    # print("Description:", result["weather"][0]["main"])
    # print("Wind Speed:", result["wind"]["speed"])
