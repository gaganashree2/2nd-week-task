import requests

# Specify the URL you want to send the GET request to
url = 'https://samples.openweathermap.org/data/2.5/weather?q=London&appid=b1b15e88fa797225412429c1c50c122a1'

# Send the GET request
response = requests.get(url)

# Check the response status code to ensure the request was successful
if response.status_code == 200:
    # The response content (HTML, JSON, etc.) can be accessed using response.text
    print(response.text)
else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')
# Parse the response content as HTML using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Check the status code of the response
if response.ok:
    # Find the div element that contains the weather data by its id
    weather_div = soup.find(id="https://samples.openweathermap.org/data/2.5/weather?q=London&appid=b1b15e88fa797225412429c1c50c122a1")

    # Check if weather_div is not None before extracting data
    if weather_div:
        try:
            # Extract the temperature, humidity, wind speed and pressure from the div element
            temperature = weather_div.find("span", class_="CurrentConditions--tempValue--3KcTQ").text
            humidity = weather_div.find("div", class_="CurrentConditions--phraseValue--2xXSr").text
            wind_speed = weather_div.find("span", class_="Wind--windWrapper--3aqXJ Wind--speedValue--1i9rw").text
            pressure = weather_div.find("span", class_="Pressure--pressureWrapper--3VmY2 Pressure--pressureValue--1YR3y").text

            # Print the extracted data
            print(f"Temperature: {temperature}")
            print(f"Humidity: {humidity}")
            print(f"Wind Speed: {wind_speed}")
            print(f"Pressure: {pressure}")
        except Exception as e:
            # Print the exception message if any error occurs
            print(f"An error occurred while extracting weather data: {e}")
    else:
        # Find out why the weather data is not found on the webpage
        message = soup.find("div", class_="MessageList--messageList--2wGRT")
        if message:
            # Print the message from the webpage
            print(message.text)
        else:
            # Print a generic message
            print("Weather data not found on the webpage.")
else:
    # Raise an exception if the status code is not 200
    response.raise_for_status()
