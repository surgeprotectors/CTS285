# -*- coding: utf-8 -*-
"""
CTS 285
Dataman Menu
Caleb Watson
12/9/2020
"""
from answerChecker import *
from memoryBank import *


def main():
    print("GREETINGS! BEHOLD THE GLORY OF THE DATAMAN CALCULATOR!")
    print("SELECT WHAT YOU'D LIKE TO DO TODAY!")
    
    # menu loop
    userinput = " "
    
    while userinput != 3:
        print("Press 1 to use the Answer Checker to solve a single problem!")
        print("Press 2 to enter the Memory Bank!")
        print("Press 3 to exit DATAMAN!")
        userinput = int(input("Enter your option: "))
        
        if userinput == 1:
            print("\n")
            answerChecker()
        elif userinput == 2:
            print("\n")
            bankMenu()
        elif userinput == 3:
            print("\n")
            print("Exiting DATAMAN")
        else:
            print("UNKNOWN EXCEPTION! USER INPUT VARIABLE OUT OF BOUNDS!")
            
main()