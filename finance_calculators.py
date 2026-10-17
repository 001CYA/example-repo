import math
# Python Code:

# Display the service menu to the user in the terminal
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.")

# Capture choice and force lowercase normalization to ensure case-insensitivity
user_choice = input("Enter either “investment” or “bond” from the menu above to proceed: ").lower()

# Route execution path based on the validated application mode
if user_choice == "investment":
    print("Successful: You chose investment.")
elif user_choice == "bond":
    print("Successful: You chose bond.")

# Fallback catch-all to handle malformed or unsupported inputs defensively
else:
    print("Error: Invalid entry. Please type either 'investment' or 'bond'.")

# Process the investment option path
if user_choice == "investment":
    # Request financial metrics and cast inputs to appropriate numerical types
    investment_deposit = float(input("Enter the amount of money you want to deposit: "))
    investment_rate = float(input("Enter the interest rate (as a number, e.g, 8): "))
    investment_years = int(input("Enter the number of years: "))

    # Normalize interest selection to lowercase to handle mixed-case inputs
    investment_interest = input("Do you want 'simple' or 'compound' interest: ").lower()

    # Convert the annual percentage rate to a decimal value (e.g., 8 becomes 0.08)
    r = investment_rate / 100

    # Simple Interest Calculation Strategy: A = P(1 + r * t)
    if investment_interest == "simple":
        total_amount = investment_deposit * (1 + r * investment_years)
        print(f"The total after {investment_years} years will be: R{total_amount:.2f}")

    # Compound Interest Calculation Strategy: A = P(1 + r)^t
    elif investment_interest == "compound":
        total_amount = investment_deposit * math.pow((1 + r), investment_years)
        print(f"The total after {investment_years} years will be: R{total_amount:.2f}")

    # Input validation fallback for invalid interest calculations
    else:
        print("Error: Invalid entry. Please type either 'simple' or 'compound'.")

# Process the bond/home loan option path
elif user_choice == "bond":
    # Request bond metrics and cast inputs to appropriate numerical types
    house_value = float(input("Enter the value of the house, (e.g 100000): "))
    bond_rate = float(input("Enter the interest rate (as a number, e.g, 7): "))
    bond_months = int(input("Enter the number of months: "))

    # Calculate monthly interest rate (i) by converting annual percent to decimal and dividing by 12 months
    i = bond_rate / 100 / 12

    # Calculate monthly bond repayment amount using the loan formula: repayment = (i * P) / (1 - (1 + i)^-n)
    bond_repayment = (i * house_value)/(1 - (1 + i)**(-bond_months))

    # Output the calculated monthly repayment formatted to 2 decimal places for currency
    print(f"Your monthly bond repayment will be: R{bond_repayment:.2f}")

# Fallback catch-all to handle malformed menu inputs defensively
else:
    print("Invalid input. Please try again.")
