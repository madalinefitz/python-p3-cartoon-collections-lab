def roll_call_dwarves(dwarves_names):
    for index, value in enumerate(dwarves_names, 1):
        print(f"{index}. {value}")

def summon_captain_planet(planeteer_calls):
    new_list = [ f"{element.capitalize()}!" for element in planeteer_calls]
    return(new_list)
    

def long_planeteer_calls(long_words):
    for word in long_words:
        if len(word) > 4:
            return True
    return False
    
   

def find_the_cheese(snack_foods):
    for food in snack_foods:
        if food == "cheddar":
            return food
        elif food == "gouda":
            return food 
        elif food=="camembert":
            return food
    return None


