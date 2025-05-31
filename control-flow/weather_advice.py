"""
PSEUDOCODE
 *Program to execute base on user input
 Ask user current weather condition
 From the weather condition, the user provided, we recommend what to do
 would provide clothing recommendation base on the weather conditions


 *

"""
"""
algorithm 


prompt the user to enter the current weather condition
from the weather condition giving deduce the the type of dress the user should wear
there are just three weather condition in this  case sunny , rainy and cold
if the weather condition is sunny 
   wear a t-shirt and sunglasses 
if the weather condition is rainy
   don't forget your umbrella and rain boat
if the weather condition is cold
   Make sure you wear a warm coat a scart
else
 Sorry, I don't have recommendations for this weather
 
 display the weather condition
 display the recommended clothing

"""
user_current_weather_condition = input("\nWhat's the weather like today? (sunny/rainy/cold):  ").lower()
print(user_current_weather_condition)
if user_current_weather_condition == "sunny":
    print(" wear a t-shirt and sunglasses ")
elif user_current_weather_condition == "rainy":
    print("  don't forget your umbrella and rain boat")
elif user_current_weather_condition == "cold":
    print("  wear a warm coat a scart")
else:
    print("Sorry, I don't have recommendations for this weather")




