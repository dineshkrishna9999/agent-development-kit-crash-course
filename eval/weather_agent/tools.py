def get_weather(city: str) -> dict:
    """Get weather for a city"""
    
    # Simple weather data
    weather = {
        "chennai": "Sunny, 32°C",
        "new york": "Sunny, 22°C",
        "london": "Rainy, 15°C", 
        "tokyo": "Cloudy, 28°C",
        "paris": "Sunny, 18°C",
        "sydney": "Windy, 25°C"
    }
    
    city_name = city.lower().strip()
    
    if city_name in weather:
        return {
            "status": "success",
            "result": f"Weather in {city.title()}: {weather[city_name]}"
        }
    else:
        return {
            "status": "error", 
            "result": f"No weather data for {city}. Try: New York, London, Tokyo, Paris, Sydney"
        } 