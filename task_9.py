print("") # introduces calculator and menu of operations that can be performed
print("This is your Simple Calculator!")
print("You will be asked to pick an operation to perform and two numbers.")
print("")
print('''The operations you can perform are:
+ for Add
- for Subtract
* for Multiply
/ for Divide
> to Exit
''') 
file = open("equations.txt", "w") #creates text file to store user input equations
# used geeksforgeeks on how to create, write and read text file https://www.geeksforgeeks.org/reading-writing-text-files-python/


while True :
    menu = input("Please select what you would like to do from the menu above: + | - | * | / | > : ") #checks choice from menu
    print("") 

    if menu in ("+", "-", "*", "/") :  #user chooses + - / or * user asked first and second number
        try :
            num_1 = float(input("Please enter your first number: "))
            num_2 = float(input("Please enter your second number: "))


        except ValueError : #if  value error found, user continues menu loop
            print("You have not entered a valid number!")
            print("")
            continue

            # based on operation chosen from, prints calculations. Writes all the following calculations user made into text file
        if menu == "+" : 
            total_1 = num_1 + num_2 # used feedback from task 1 to store answers generated from calculations to write into text file
            print(f"{num_1} + {num_2} = {num_1 + num_2}")
            file.write(str(num_1)+" "+menu+" "+str(num_2)+" " "=" " "+str(total_1)+"\n") # used adamsmith to convert float to string to write in text file

        elif menu == "-" :
            total_2 = num_1 - num_2
            print(f"{num_1} - {num_2} = {num_1 - num_2}")
            file.write(str(num_1)+" "+menu+" "+str(num_2)+" " "=" " "+str(total_2)+"\n")

        elif menu == "*" :
            total_3 = num_1 * num_2
            print(f"{num_1} x {num_2} = {num_1 * num_2}")
            file.write(str(num_1)+" "+menu+" "+str(num_2)+" " "=" " "+str(total_3)+"\n")

        elif menu == "/" :
            if num_2 == 0 : #prints if zero error detected 
                print("You cannot divide by zero.") # used Rollbar when came accross zerodivision error and how this can be fixed https://rollbar.com/blog/python-zerodivisionerror/#:~:text=A%20ZeroDivisionError%20occurs%20in%20Python,Python%20code%20raises%20a%20ZeroDivisionError%20.

            else: 
                total_4 = num_1 / num_2
                print(f"{num_1} / {num_2} = {num_1 / num_2}")
                file.write(str(num_1)+" "+menu+" "+str(num_2)+" " "=" " "+str(total_4)+"\n")

    elif menu == ">" :
        exit = input("Would you like to display your calculated equations before leaving? - yes / no: ").lower()
        if exit == "yes":
            equations = input("Please enter equations.txt to display calculated equations: ")
            
            while True:
             if equations == "equations.txt" :
                        file = open('equations.txt', 'r') #read text file
                        print("")
                        print("Please find below the equations you have calculated:")
                        print(file.read())
                        break

             else: print("The file you want to open does not exist") # if it does not exit, this will print
             equations = input("Please enter equations.txt to display equations you have calculated: ")
             continue   
            
        elif exit == "no" :
            print("Thank you for using the Calculator. Goodbye!") #user can exit calculator leaving loop
            break 

        else: print("You have not made a valid choice.")

    else: print("You have not selected from the menu.")
    print("")# invalid input and menu printed and user enters menu loop
    
    calculate = input("Would you like to continue?- yes / no: ").lower()
    print("")

    if calculate == "yes" :
        continue  #continues menu loop
    while True: 
        if calculate == "no" : # asks user if they would like to display equations or return to main menu
            choice = input("Would you like to display equations or return to main menu? - display / return: ").lower()
            print("")

            if choice == "display" : # user must type in text file name
                equations = input("Please enter equations.txt to display calculated equations you have calculated: ")
            
                while True :
                    if equations == "equations.txt" :
                        file = open('equations.txt', 'r') #read text file
                        print("")
                        print("Please find below the equations you have calculated:")
                        print(file.read())
                        break

                    else: print("The file you want to open does not exist") # if it does not exit, this will print
                    equations = input("Please enter equations.txt to display equations: ")
                    continue

            else:
                choice == "return"  # user can exit calculator  
                print("")
                break
        else:
            print("You have not made a valid choice.") # no valid choice prints from no invalid input
            print("")
            break
file.close()        
