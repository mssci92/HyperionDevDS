import math

home = "bond" 
deposit = "investment"

sim_interest = "simple"
com_interest = "compound"

# The menu will print of the two types of calculators that the user can choose, Bond and Investment. 
# User will be asked to type in calcualtor they want to use. String of capitalized and upper characters converted to lower to ensure entries are read
# User required to input information depending on calculator choice and calculation is displayed.
# If no calculator not picked user will be told to try again

print("The Investment calculator is used to calculate the amount of interest you'll earn on your investment.\n")

print("The Bond calculator is used to calculate the amount you'll pay on a home loan.\n")

menu = input("\nPlease enter either " + home + " or " + deposit + " from the menu above to begin: ").lower()


if menu == home :
    print("You have chosen the Bond Calculator.")
    value = float(input("Please enter the value of the house: "))
    rate = float(input("Please enter the interest rate: "))
    months = int(input("Please enter the number of months you plan to repay the bond: "))
    monthly_rate = (rate / 100) / 12
    repayment = (monthly_rate * value) / (1 - (1 + monthly_rate)**(- months))
    print("Each month you will repay" ,repayment, "GBP.")


elif menu == deposit :
    print("You have chosen the Investment Calculator.")
    deposit_in = float(input("Please enter the amount you wish to deposit: "))
    rate = float(input("Please enter the interest rate number only: "))
    years = int(input("Please enter the number of years you wish to invest: "))
    monthly_rate =  rate / 100
    interest = input("Please enter whether you wish to calculate " + sim_interest +  " or " + com_interest + " interest: ").lower()
    

    if interest == sim_interest:
        total_sim = deposit_in * (1 + monthly_rate*years)
        print("Your will get back after" , years ,"years" , total_sim , "GBP at an interest rate of" , rate ,"%.")

    elif interest == com_interest:
        total_com = deposit_in * math.pow((1+monthly_rate), years)
        print("Your will get back after" , years ,"years" , total_com , "GBP at an interest rate of " , rate ,"%." )


else :
    print("You have not entered the name of the calculator from the menu. Please try again.")