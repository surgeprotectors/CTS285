# -*- coding: utf-8 -*-
"""
CTS 285
Dataman Memory Bank
Caleb Watson
12/9/2020
"""

def writeToBank():
    with open('bank.txt', mode='w') as bank:
        for i in range(10):
            # store variables
            print("Problem #" + str(i+1))
            num1 = input("Enter the first number in your equation: ")
            operator = input("Enter '+', '-', '*', or '/' to perform the corresponding operation in your equation: ")
            num2 = input("Enter the second number in your equation: ")
            # write
            bank.write(num1 + " " + operator + " " + num2 + "\n")
        
    # exit writeToBank()
    print("Done writing to Memory Bank!\n")
    
        
def runBank():
    # initialize score
    score = 0
    # loop through file
    with open('bank.txt', mode='r') as bank:
        for record in bank:
            num1, operator, num2 = record.split()
            print(record)
            # calculate correct answer
            if operator == "+":
                answer = int(num1)+int(num2)
            elif operator == "-":
                answer = int(num1)-int(num2)
            elif operator == "*":
                answer = int(num1)*int(num2)
            elif operator == "/":
                longAnswer = int(num1)/int(num2)
                answer = float("%.2f" % longAnswer)
            # user inputs answer
            if operator == "/":
                print("Round all division answers to the second decimal place.")    
            
            if operator == "/":
                userGuess = float(input("What do you think is the correct answer to this question?: "))
                userGuess = float("%.2f" % userGuess)
            else:
                userGuess = int(input("What do you think is the correct answer to this question?: "))
            # check userAnswer vs answer, add score if necessary
            if userGuess == answer:
                print("You are correct!")
                score += 1
            else:
                print("The correct answer is " + str(answer) + ".")
    
    # display score and exit runBank()
    print("Your score is: " + str(score))
    if score >= 10:
        print("GREAT JOB!")
    print("Exiting test!\n")



def bankMenu():
    # menu loop
    userinput = " "
    
    while userinput != 3:
        print("Welcome to the Memory Bank!")
        print("Press 1 to store a series of 10 problems for later")
        print("Press 2 to run the test!")
        print("Press 3 to exit the Memory Bank")
        userinput = int(input("Enter your option: "))
        
        if userinput == 1:
            print("\n")
            writeToBank()
        elif userinput == 2:
            print("\n")
            runBank()
        elif userinput == 3:
            print("\n")
            print("Exiting Memory Bank")
        else:
            print("UNKNOWN EXCEPTION! USER INPUT VARIABLE OUT OF BOUNDS!")
