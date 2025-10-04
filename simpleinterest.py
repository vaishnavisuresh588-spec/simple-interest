# Simple and Compound Interest Calculator

# Taking inputs from the user
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of Interest (%): "))
time = float(input("Enter the Time (in years): "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Calculating Compound Interest
compound_interest = principal * ((1 + rate / 100) ** time) - principal

# Displaying the results
print("\n--- Interest Calculation Results ---")
print(f"Simple Interest = {simple_interest:.2f}")
print(f"Compound Interest = {compound_interest:.2f}")

# Optional: show total amount for each
print(f"Total Amount (with Simple Interest) = {principal + simple_interest:.2f}")
print(f"Total Amount (with Compound Interest) = {principal + compound_interest:.2f}")
