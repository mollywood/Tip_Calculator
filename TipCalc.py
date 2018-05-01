total_amount = int(input("Enter the total amount: "))
tip_percent = int(input("What percentage would you like to tip? "))
tip_per = tip_percent * .01
actual_tip = total_amount * tip_per
print(f"The tip should be ${actual_tip}.")
