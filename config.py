BOT_API_TOKEN = '5754703308:AAEG7v5vwXCtfqOFomCre0XYwToQ-myndOI'
WEATHER_API_KEY = 'e167adb8ac5f97395df1e2e53f3d0863'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric' + '&lang=ua'
)