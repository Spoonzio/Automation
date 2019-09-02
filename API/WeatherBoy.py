import json, requests

def curr_weather (fcity):
    try:
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ fcity.strip() +"&appid=886705b4c1182eb1c69f28eb8c520e20")
        response.raise_for_status()
    except Exception as e:
        print(e)

    if response.status_code == 200:
        weather_data = json.loads(response.text)
        weather = weather_data["weather"][0]["main"]
        weather +=", " + weather_data["weather"][0]["description"]

        temper = weather_data["main"]["temp"]
        min_temper = weather_data["main"]["temp_min"]
        max_temper = weather_data["main"]["temp_max"]

        print("\nIn " +fcity.title() +":\n" 
                +"Weather: " +weather +"\n" 
                +"Current Temp: " + str(round(temper,2)) +"\n" 
                +"Lowest Temp: " +str(round(min_temper,2)) +"\n"
                +"Highest Temp: " +str(round(max_temper,2)))
    
    elif response.status_code == 404:
        print("Server is offline!")

city = str(input("What city would you like to check:\n"))
curr_weather(city)