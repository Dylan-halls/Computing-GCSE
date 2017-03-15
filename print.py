def cal(mass_of_liquid, temperature_at_start, temperature_at_end,
        specific_heat_capacity_water):
    #Calculate DeltaT
    temperature_change = temperature_at_end - temperature_at_start
    #Calculate DeltaH
    energy_added = mass_of_liquid * specific_heat_capacity_water * temperature_change
    #Output the result
    return energy_added, energy_added/1000


specific_heat_capacity_water = 4.2
run = True

while run == True:
    try:
        mass_of_liquid = float(input("What mass of water did you use? (g) "))
        temperature_at_start = float(input("What was your starting temperature? (K) "))
        temperature_at_end = float (input("What was your final temperature? (K) "))
    except ValueError: print("Needed Number"); exit()

    e_added, e_kj = cal(mass_of_liquid, temperature_at_start, temperature_at_end, specific_heat_capacity_water)
    print ("Your water changed in energy by",e_added,"J")
    print ("That is",e_kj,"KJ")
    choice = input ("Would you like to have another go? Y/N ").lower()
    if choice == "n":
        run = False
print ("Program Finished")
