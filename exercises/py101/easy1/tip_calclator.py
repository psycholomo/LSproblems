bill = input("What is the bill?" \
"n")
tip = input("What is the tip percentage?")

bill = int(bill)
tip = int(tip)

print(f"The tip is ${bill * (percentage / 100)}")
print(f"The total is ${bill + tip}")