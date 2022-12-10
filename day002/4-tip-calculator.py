print("Welcome to the tip calculator.")

subtotal = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = subtotal * (tip_percent / 100)

total = subtotal + tip

print(f"Each person should pay: ${'{:.2f}'.format(round(total / people, 2))}")

