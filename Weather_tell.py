DIRECTION_ABBREVIATIONS = ['N', 'NNE', 'NE', 'NEE', 'E', 'SEE', 'SE', 'SSE',
                           'S', 'SSW', 'SW', 'SWW', 'W', 'NWW', 'NW', 'NNW']
DIRECTION_ABBREVIATIONS_LOWERCASE = ['n', 'nne', 'ne', 'nee', 'e', 'see', 'se', 'sse',
                                     's', 'ssw', 'sw', 'sww', 'w', 'nww', 'nw', 'nnw']


# Convert azimuth (measured in degrees) into abbreviation
# Abbreviations:  N, NNE, NE, NEE, E, SEE, SE, SSE, S, SSW, SW, SWW, W, NWW, NW, NNW
# Note, for exact "bisector" directions such as N-NNE (for this one x=11.25),
# the shorter abbreviation is returned.
def direction_deg_to_abbr(x):
    x1 = x % 360.0
    if x1 <= 11.25:
        return "N"
    elif x1 < 33.75:
        return "NNE"
    elif x1 <= 56.25:
        return "NE"
    elif x1 < 78.75:
        return "NEE"
    elif x1 <= 101.25:
        return "E"
    elif x1 < 123.75:
        return "SEE"
    elif x1 <= 146.25:
        return "SE"
    elif x1 < 168.75:
        return "SSE"
    elif x1 <= 191.25:
        return "S"
    elif x1 < 213.75:
        return "SSW"
    elif x1 <= 236.25:
        return "SW"
    elif x1 < 258.75:
        return "SWW"
    elif x1 <= 281.25:
        return "W"
    elif x1 < 303.75:
        return "NWW"
    elif x1 <= 326.25:
        return "NW"
    elif x1 < 348.75:
        return "NNW"
    else:
        return "N"


# Convert direction abbreviation into azimuth (measured in degrees)
# The input in case-insensitive.
# If the abbreviation is not known raise ValueError exception
def direction_abbr_to_deg(string):
    return 22.5 * DIRECTION_ABBREVIATIONS_LOWERCASE.index(string.lower())


# t is a temperature in degrees Celsius
def temperature_to_word(t):
    if t < 0:
        return 'Freezing'
    elif t < 7:
        return 'Chilly'
    elif t < 20:
        return 'Cool'
    elif t <= 28:
        return 'Warm'
    else:
        return 'Hot'


# wind_speed is in m/s
def wind_speed_to_word(wind_speed):
    if wind_speed < 1.54333:
        return 'calm'
    else:
        return 'windy'


# Weather to print the wind direction?
# wind_speed is in m/s
def is_windy(wind_speed):
    return wind_speed >= 1


class Weather:
    """The class to describe temperature and wind."""
    def __init__(self, temperature, wind_speed, wind_direction):
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

    def print(self):
        print(f"Temperature: {self.temperature} C.")
        print(f"Wind: speed {self.wind_speed} m/s, direction {self.wind_direction} deg.")

    # Next function is not intended to be inherited.
    # Thus, VerbalWeather.input() will return an object of class Weather, misleadingly.
    @staticmethod
    def input():
        input_string = input("Temperature (deg C): ")
        input_temperature = float(input_string)
        input_string = input("Wind speed (km/h): ")
        input_wind_speed = float(input_string)
        input_string = input("Wind direction (azimuth in deg or abbreviation): ")
        try:
            input_wind_direction = direction_abbr_to_deg(input_string)
        except ValueError:
            input_wind_direction = float(input_string)
        return Weather(temperature=input_temperature,
                       wind_speed=input_wind_speed, wind_direction=input_wind_direction)


class VerbalWeather(Weather):
    """Class used to print \"weather string\"."""

    # VerbalWeather(weather_object) is used to cast the instance of class Weather
    # into an instance of class VerbalWeather
    def __init__(self, weather_object):
        Weather.__init__(self,
                         temperature=weather_object.temperature,
                         wind_speed=weather_object.wind_speed,
                         wind_direction=weather_object.wind_direction)
        self.temperature_word = None
        self.wind_speed_word = None
        self.wind_direction_abbr = None
        self.weather_string = ""

    def update_weather_string(self):
        self.temperature_word = temperature_to_word(self.temperature)
        self.wind_speed_word = wind_speed_to_word(self.wind_speed)
        self.wind_direction_abbr = direction_deg_to_abbr(self.wind_direction)
        if is_windy(self.wind_speed):
            self.weather_string = f"{self.temperature_word}, {self.wind_speed_word}, {self.wind_direction_abbr} wind."
        else:
            self.weather_string = f"{self.temperature_word}, {self.wind_speed_word}."

    def print(self):
        self.update_weather_string()
        print(self.weather_string)


# Main program
try:
    # Calling a static method
    # If the method were not decorated, "the_weather = Weather.input(None)" would work
    the_weather = Weather.input()
except ValueError:
    print("Sorry, the input is not correct.")
else:
    the_weather.print()
    verbal_weather = VerbalWeather(the_weather)
    # Calling an overriding method
    verbal_weather.print()
    # Calling an overridden method of the parent class
    Weather.print(verbal_weather)
