# """
# PSEUDOCODE
#  *Program to execute base on user input
#  Ask user current weather condition
#  From the weather condition, the user provided, we recommend what to do
#  would provide clothing recommendation base on the weather conditions


#  *

# """
# """
# algorithm 


# prompt the user to enter the current weather condition
# from the weather condition giving deduce the the type of dress the user should wear
# there are just three weather condition in this  case sunny , rainy and cold
# if the weather condition is sunny 
#    wear a t-shirt and sunglasses 
# if the weather condition is rainy
#    don't forget your umbrella and rain boat
# if the weather condition is cold
#    Make sure you wear a warm coat a scart
# else
#  Sorry, I don't have recommendations for this weather
 
#  display the weather condition
#  display the recommended clothing

# """
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
# print(user_current_weather_condition)
if weather == "sunny":
    print(" Wear a t-shirt and sunglasses.\n ")
elif weather == "rainy":
    print("don't forget your umbrella and raincoat\n")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.\n")
else:
    print("Sorry, I don't have recommendations for this weather\n")




