import random

def diceRoller(diceCount, diceType, mod):
 #create list for later use of dice roll results
    diceList = [mod]
                
    #for every value in the range of dice count we will execute the following loop
    for i in range(diceCount):
        #diceRoll is our new variable which will be an int between 1 and the diceType
        diceRoll = random.randint(1,diceType)
        
        #add the diceRoll variable to our diceList
        diceList.append(diceRoll)
        
        #if the value i isn't less than diceCount -1 (meaning if we are not at the last value in the loop)
        #then we print a the diceRolls in a string with + and remove the space at the end
        #this is formatting that tells python not too print each diceRoll on a new line
        """if i != diceCount - 1:
            print(str(diceRoll)+ " + ", end="")
        else:
            print(str(diceRoll))"""
    #our final variable equals the sum of our diceList
    diceTotal = sum(diceList)
    #must specify return value for function
    return diceTotal

#create list to keep track of roll history
rollHistory = []

#creates an infinite loop of instructions
while True:
    #user input creates userRoll variable
    userRoll = input("What are we rolling? Enter history if you want to view all past rolls.\n")
    #this ensures that any way history is entered it will be recalled properly
    if userRoll.upper() == "HISTORY":
        for r in rollHistory:
            print(r)
        continue
    #continue user entered varibales
    mod = input("Are there any modifiers?\nPlease use positive or negative integer.If none, enter zero.\n")
    condition = int(input("Are you rolling regularly (0) or with advantage (1) or disadvantage (2)?\n"))
    #add parameters to match with condition
    parameters = [' ', 'with advantage', 'with disadvantage']
                
    #take variable roll and split by string d
    userRoll = userRoll.split("d")
       
    #establish variable strings as int variables
    diceCount = int(userRoll[0])
    diceType = int(userRoll[1])
    mod = int(mod)
            
    #print the number of dice and type of dice
    print("We are rolling " + str(diceCount) + " d" + str(diceType) + " dice " + parameters[condition] \
          + " and a modifier of " + str(mod))
    print("Your roll total is ", end="")
    
   #here we review the actions if certain conditions are met; if the condition is entered as 0, 1, or 2 then different paths will execute and compare results.
    if condition == 0:
        roll = diceRoller(diceCount, diceType, mod)
        print(roll)
        rollHistory.append(str(diceCount)+"d"+str(diceType)+'mod '+str(mod)+' = '+str(roll))
        
    elif condition == 1:
        rollOne = diceRoller(diceCount, diceType, mod)
        rollTwo = diceRoller(diceCount, diceType, mod)
        if rollOne > rollTwo:
            print(rollOne)
            rollHistory.append(str(diceCount)+"d"+str(diceType)+'mod '+str(mod)+' advantage = '+str(rollOne))
        else:
            print(rollTwo)
            rollHistory.append(str(diceCount)+"d"+str(diceType)+'mod '+str(mod)+' advantage = '+str(rollTwo))
        
    elif condition == 2:
        rollOne = diceRoller(diceCount, diceType, mod)
        rollTwo = diceRoller(diceCount, diceType, mod)
        if rollOne < rollTwo:
            print(rollOne)
            rollHistory.append(str(diceCount)+"d"+str(diceType)+'mod '+str(mod)+' disadvantage = '+str(rollOne))
        else:
            print(rollTwo)
            rollHistory.append(str(diceCount)+"d"+str(diceType)+'mod '+str(mod)+' disadvantage = '+str(rollTwo))
    
    print(" ")
