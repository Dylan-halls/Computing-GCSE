#These are my variables
temperature_at_start = 0.0
temperature_at_end = 0.0
temperature_change = 0.0
mass_of_liquid = 0.0
energy_added = 0.0
runagain = True
choice="Y"
#These are my constants
specific_heat_capacity_water = 4.2
#Welcome the user
print ("Hello and welcome to DeltaH")
while runagain == True:
    #Ask for the data
    mass_of_liquid = float ( input ("What mass of water did you use? (g) "))
    temperature_at_start = float ( input ("What was your starting temperature? (K) "))
    temperature_at_end = float ( input ("What was your final temperature? (K) "))
    #Calculate DeltaT
    temperature_change = temperature_at_end - temperature_at_start
    #Calculate DeltaH
    energy_added = mass_of_liquid * specific_heat_capacity_water * temperature_change
    #Output the result
    print ("Your water changed in energy by",energy_added,"J")
    #Convert J to KJ
    print ("That is",energy_added/1000,"KJ")
    choice = input ("Would you like to have another go? Y/N ")
    if choice == "N":
        runagain = False
    else:
        runagain = True
print ("Program Finished")


