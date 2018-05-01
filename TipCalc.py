# ask the user to input the amounts
total_amount = int(input("Enter the total amount: "))
tip_percent = int(input("What percentage would you like to tip? "))
# calculate the percentage by make tip_percent a decimal
tip_per = tip_percent * .01
#calculate the appropriate tip amount
actual_tip = total_amount * tip_per
print(f"The tip should be ${actual_tip}.")
