print("Welcome to the tip calculator")
bill_amount=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give?10 12 or 15: "))
people=int(input ("How many people would you like to split the bill amount? "))
final=((tip/100*bill_amount)+bill_amount)/people
print(f"Each person should pay: ${round(final,2)}")
