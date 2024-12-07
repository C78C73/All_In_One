from time import sleep
import random, string

#main menu
def mainMenu():
    while True:
        print("\nChoose an option: ")
        print("\n 1 - Calculator")
        print(" 2 - Timer")
        print(" 3 - Password Generator")
        chosenOption = int(input("\nOption: "))
        
        if (chosenOption == 1):
            theCalc()    
        elif (chosenOption == 2):
            theTimer()
        elif (chosenOption == 3):
            passwordGen()
        else:
            continue
    
#the calc
def theCalc():
    print("\n------------\nCalculation\n------------\n")
    
    while True:        
        operator = ['+', '-', '*','/']  
        
        try: 
            theEquation = input((f"Enter the calculation (use spaces):  "))
        
            parts = theEquation.split()
            x = float(parts[0])
            operator = parts[1]
            y = float(parts[2])
            
            if (operator == '+'):
                result = x + y
            elif (operator == '-'):
                result = x - y
            elif (operator == '*'):
                result = x * y
            elif (operator == '/'):
                result = x / y
            else:
                return theEquation
            
            print(f"\n{x} {operator} {y} = {result:.2f}")
        except Exception as Error:
            print(f"\nError: {Error}")
        
        goBack = str(input("\nGo back or do another calculation? (exit/calc): ")).lower()
        if (goBack == 'calc'):
            continue
        elif (goBack == 'exit' ):
            return mainMenu()
        else:
            print("\nError: Invalid input")
            return theEquation
        
#the timer
def theTimer():
    print("\n------------\nTimer\n------------")
    
    while True:
        timerTime = int(input("\nSet the time limit: "))
        
        for x in range(0, timerTime+1, 1):
            print(f"\n{x} second(s)")
            sleep(1)

        print("Done.")
        goBack = str(input("\nGo back or do another calculation? (exit/timer): ")).lower()
        if (goBack == 'timer'):
            continue
        elif (goBack == 'exit' ):
            return mainMenu()
        else:
            print("\nError: Invalid input")
            continue

# the password generator
def passwordGen():
    print("\n------------\nPassword Generator\n------------")
    
    while True:
        passwordLength = int(input("How long do you want the password to be: "))
        print("")
        
        theRandomizer = random.SystemRandom()
        thePassword = ''.join(theRandomizer.choice(string.digits + string.ascii_letters) for _ in range(passwordLength))
        
        for x in range(3, 0, -1):  
            print("Generating password" + "." * x)  
            sleep(1)
        
        print(f"\nYour new password is - {thePassword}")
    
        goBack = str(input("\nGo back or do another calculation? (exit/timer): ")).lower()
        if (goBack == 'timer'):
            continue
        elif (goBack == 'exit' ):
            return mainMenu()
        else:
            print("\nError: Invalid input")
            continue
    
mainMenu()