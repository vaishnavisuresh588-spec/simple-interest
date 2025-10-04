# Simple Interest Calculator

# Taking inputs from the user
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of Interest (%): "))
time = float(input("Enter the Time (in years): "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Displaying the result
print("The Simple Interest is:", simple_interest)

