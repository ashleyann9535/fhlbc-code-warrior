#Exercise 29 - Dictionary Access
#Print out a string depending on if food  is a value in bakery_stock .If food  is contained 
#in bakery_stock  print out a string that states how many items are left: "3 left" 
#if food is "toffee cookie" or "1 left" if food is "morning bun", etc.
#If food is not contained in bakery_stock  (like "gummy bear"), print out "We don't make that"

# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}
# YOUR CODE GOES BELOW:
if food in bakery_stock:
    print(f"{bakery_stock[food]} left")
else:
    print("We don't make that")

#Exercise 30 - Fromkeys Exercise
#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 
# Use the game_properties list and dict.fromkeys() to generate a dictionary 
# with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state= {}.fromkeys(game_properties, 0)
print(initial_game_state)