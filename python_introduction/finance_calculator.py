monthly_income = int(input("Enter your monthly income:"))
total_expense = int(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - total_expense
projected_Savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_Savings}.")
