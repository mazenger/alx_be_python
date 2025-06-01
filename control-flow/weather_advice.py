#!/usr/bin/env python3
"""
Weather Advice Script
This script provides clothing recommendations based on weather conditions.
"""

def get_weather_recommendation(weather):
    """
    Returns clothing recommendations based on weather conditions.
    
    Args:
        weather (str): The current weather condition
        
    Returns:
        str: Clothing recommendation for the given weather
    """
    if weather.lower() == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather.lower() == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather.lower() == "cold":
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

def main():
    # Prompt user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ")
    
    # Get and print the recommendation
    recommendation = get_weather_recommendation(weather)
    print(recommendation)

if __name__ == "__main__":
    main() 