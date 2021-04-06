#!/usr/bin/env python3
# create the list called farms
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


# loop across the 3 farms that we have
for x in farms:
    
    farm = x.get("name")  # extract the farm name
    agriculture = x.get("agriculture") # extract the farm crops

    print("The farm is:", farm)  # each time through the loop print value of x
    print(f"The farm grows:")
    for crop in agriculture:
        print(f"  - {crop}")
    



print("\nOur loop has ended.")  # when the loop ends print this

