# -*- coding: utf-8 -*-
"""
CTS 285
Combat Test
Caleb Watson
10/20/2020
"""



def combatMenu():
    """ a function that handles the combat menu """
    userInput = int(input("1) ATTACK\n2) DEFEND\nCHOOSE YOUR ACTION: "))
    if userInput == 1:
        return "ATTACK"
    elif userInput == 2:
        return "DEFEND"
    
def playerDamageCalc(userInput, playerHP, enemyHP, turnNumber):
    """ a function for handling combat damage """
    # player's action
    if userInput == "ATTACK":
        print("You slash the foe for 20 damage.")
        enemyHP = enemyHP - 20
    elif userInput == "DEFEND":
        print("You assume a defensive position.")
    # enemy action
    if enemyHP > 0:
        if userInput == "DEFEND":
            print("You block the enemy's attack!")
        elif (turnNumber%2) == 0:
            print("The orc strikes you for 10 damage and starts frothing angrily...")
            playerHP = playerHP - 10
        else:
            print("The orc delivers a gruesome blow! You bleed for 40 damage! The orc looks tired after that strike.")
            playerHP = playerHP - 40
            
    # advance turnNumber and return variables
    turnNumber += 1
    return playerHP, enemyHP, turnNumber
    
def main():
    """ testing functionality """
    # initialize variable
    playerHP = 100
    enemyHP = 100
    
    # start the fight
    print("You are confronted by an orc!\n")
    turnNumber = 0
    
    # combat loop
    while playerHP > 0 and enemyHP > 0:
        menuOption = combatMenu()
        playerHP, enemyHP, turnNumber = playerDamageCalc(menuOption, playerHP, enemyHP, turnNumber)
    
    # end combat
    if playerHP <= 0:
        print("You crumple into a heap. Your story ends here.")
    elif enemyHP <= 0:
        print("The orc has been slain, you live to fight another day...")
    else:
        print("what a curious issue...this is a debug message. i dont know how this was triggered.")


main()