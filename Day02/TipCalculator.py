# Taking user input for bill amount, tip percentage, and number of people to split the bill
bill_amount = float(input("Enter the bill amount: $"))
tip_percentage = int(input("Enter the tip percentage (e.g., 15 for 15%): "))
persons = int(input("Enter the number of people to split the bill: "))

#calculating the tip amount, total amount including the tip, and amount per person
tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / persons

# printing the results
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount (including tip): ${total_amount:.2f}")
print(f"Amount per person: ${amount_per_person:.2f}")
# This code calculates the tip amount, total amount including the tip, and the amount each personl