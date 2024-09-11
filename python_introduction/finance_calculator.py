monthly_income = input("Enter your monthly income:")
monthly_expense =input("Enter your total monthly expenses:")

monthly_savings = float(monthly_income) - float(monthly_expense)
projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${round(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${round(projected_Savings)}.")
