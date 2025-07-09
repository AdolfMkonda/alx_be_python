# A program That calculate and provide feedback on a user’s monthly savings and potential future savings 
# without applying conditional statements.
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_expenses - monthly_income
projected_saving = float(monthly_savings) * 12 + float(monthly_savings) * 12 * 0.05
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_saving}.")
