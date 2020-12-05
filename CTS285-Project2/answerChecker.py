# -*- coding: utf-8 -*-
"""
CTS 285
Dataman Answer Checker
Caleb Watson
11/1/2020
"""



# user inputs equation
num1 = input("Enter the first number in your equation: ")
operator = input("Enter '+', '-', '*', or '/' to perform the corresponding operation in your equation: ")
num2 = input("Enter the second number in your equation: ")

# computer calculates answer to equation
if operator == "+":
    answer = int(num1)+int(num2)
elif operator == "-":
    answer = int(num1)-int(num2)
elif operator == "*":
    answer = int(num1)*int(num2)
elif operator == "/":
    longAnswer = int(num1)/int(num2)
    answer = float("%.2f" % longAnswer)
else:
    print("I did not detect a valid operator in this equation. I'm sorry :(")

# user inputs answer
if operator == "/":
    print("Round all division answers to the second decimal place.")    

userGuess = int(input("What do you think is the correct answer to this question?: "))

# computer responds with "correct" or "incorrect" followed by the right answer if the user was wrong
if userGuess == answer:
    print("You are correct!")
else:
    print("The correct answer is " + str(answer) + ".")