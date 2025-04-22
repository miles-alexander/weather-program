# Weather Program 🌦️

## Overview

The Weather Program is a command-line application that provides current weather information for U.S. cities. Users can retrieve weather data by entering either the city and state, or the ZIP code. The program fetches data from the OpenWeatherMap API and displays details such as temperature, humidity, pressure, and weather descriptions.



## Authors

- [@miles-alexander](https://www.github.com/miles-alexander)


## Features

Flexible Location Input: Users can choose to search for weather information using:

    •	City and State: Enter the city name along with the state code.
    •	ZIP Code: Enter the 5-digit ZIP code of the desired location.


Detailed Weather Information: For the specified location, the program displays:

    •  	Current temperature
    •	Feels-like temperature
    •	High and low temperatures
    •	Atmospheric pressure
    •	Humidity levels
    •	Weather description (e.g., clear sky, rain)

Continuous Operation: After displaying the weather information, the program prompts the user for another search or to quit, allowing multiple queries in a single session.



## Run Locally

**Clone the Repository:**

```bash
  git clone https://github.com/miles-alexander/weather-program.git
```

**Go to the Project Directory:**

```bash
  cd weather-program
```

**Install Dependencies:**

```bash
  pip install requests
```

**Obtain an OpenWeatherMap API Key:**

```bash
  •	Register for a free account at OpenWeatherMap.
  •	Navigate to the API keys section in your account and generate a new key.
  •	Upon running the script, you will be prompted to enter your OpenWeather API key directly in the terminal.

```


## Usage

**Run the Program:**

    python weather_program.py

**Follow On-Screen Prompts:**

**Enter Your API Key:**

          Type in your API key and press Enter.

**To search by city and state:**

          Type city and press Enter.
          Enter the city name when prompted.
          Enter the 2-letter state code when prompted.

**To search by ZIP code:**

            Type zip and press Enter.
            Enter the 5-digit ZIP code when prompted.

**To exit the program:**
        
            Type q and press Enter.

**View Weather Information:**

        The program will display the current weather details for the specified location.

## Example 
```bash
Welcome to the Weather Program!
Please type 'city' to search by city and state, 'zip' to search by ZIP code, or 'q' to quit: city
Please enter city name: Winter Garden
Please enter state code: FL
The current temperature in Winter Garden is: 75°F
Feels Like: 73°F
High Temp: 78°F
Low Temp: 70°F
Pressure: 1015hPa
Humidity: 60%
Description: clear sky
```

## Error Handling

    •	Invalid Input: If the user enters an unrecognized command, the program prompts for a valid   response.
    •	City/ZIP Not Found: If the entered location is not found, the program notifies the user and prompts for another input.
    •	Network Issues: The program handles HTTP errors and connection issues gracefully, informing the user of any problems.





## Acknowledgements

OpenWeatherMap for providing the weather data API.

