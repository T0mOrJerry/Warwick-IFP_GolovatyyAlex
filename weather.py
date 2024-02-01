import requests  # Importing request module to get response from API server
from json import dump  # Importing json modul for testing data by downloading them as json file from server

API_KEY = "30e3501a5c50313843a273775138e150"  # Constant - API Key gained from API's website
weather_api_server = f"https://api.openweathermap.org/data/2.5/forecast"  # Constant - address of API server


# Function which return list of forecasts in range from 1 day up to 5
def weather_getter(place: str, days=1):  # By default it gives information only about one day
    # Restricting the input of days, as free API can give maximum 5-days forecast
    if days > 5:
        days = 5
    elif days < 1:
        days = 1
    # Stating the parameters taken from API documentation for request
    weather_params = {
        "q": place,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(weather_api_server,
                            params=weather_params)  # Making the request using server address and parameters above
    data = response.json()  # Server return data as json file, unpacking it as a dictionary
    # The following part is enabled as it used only for testing
    # with open("weather.json", "w") as file:
    #     dump(data, file)
    #
    # Filter gained data and make it readable for user
    selected_data = [data["list"][i] for i in range(0, len(data["list"]), 8)]
    selected_data = selected_data[:days]
    readable_data = []
    c = 1
    for i in selected_data:
        di = {}
        di["Day"] = i["dt_txt"]
        di["Temperature"] = i["main"]["temp"]
        di["Feels Like"] = i["main"]["feels_like"]
        di["Description"] = i["weather"][0]["description"]
        di["Humidity"] = i["main"]["humidity"]
        di["Wind Speed"] = i["wind"]["speed"]
        readable_data.append(di)
        c += 1
    return readable_data  # Function return list of dictionaries for each day


class Weather:
    def get_w(self, place):  # Get specific locations
        weather = weather_getter(place)
        return self.output(weather)  # Get weather data for a specified location

    def output(self, data):  # Change the weather data from list of dictionaries into string
        output = f""
        for i in data:
            l = f""
            for j in i:
                l += f"{j}: {i[j]}\n"
            output += l
            output += "\n"
        return output  # Return a string


class Forecast(Weather):  # Weather for the next few days in a specific location
    def get_w(self, place, days):
        weather = weather_getter(place, days)  # Weather data for the next few days
        return self.output(weather)  # Rewrite and accept additional parameters


mainloop = True  # While loop condition we put it as true to run the while loop
w = Weather()  # Shortcut of the class Weather
f = Forecast()  # Shortcut of the class Forecast
print("Welcome to the Weather Forecast Application!\n")
while mainloop:  # starting the program and it will continue until we break the while loop
    x = input(
        "1.Get current weather conditions\n2.Get forecast\n3. Exit\n Enter your choice:1/2/3:")  # Explaining and asking the user to choose whatever they want
    if x == '1':
        try:  # To avoid error input
            print(w.get_w(input("Type the place: ")))  # Calling the method for the current weather from weather class
        except Exception:
            print(
                "Some error occured: try to check your connection or check the spelling of your location\n")  # Checking the spellining
    elif x == '2':
        try:  # To avoid error input
            print(f.get_w(input("Type the place: "), int(input(
                "Type amount of the days: "))))  # Calling the method from class Forecast and asking about the number of days
        except TypeError:
            print('Amount of days must be an integer!\n')
        except Exception:
            print("Some error occured: try to check your connection or check the spelling of your location\n")
    elif x == '3':
        mainloop = False  # breaking while loop by make the condition of while loop false
    else:
        print("put invalid value")
