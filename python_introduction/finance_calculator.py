# A program That calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.
monthlyIncome = int(input("Enter your monthly income: "))
monthlyExpenses = int(input("Enter your total monthly expenses: "))
ms = float(monthlyExpenses) - float(monthlyIncome)
print("Your monthly savings are ",ms)
print("Projected savings after one year, with interest, is: ",ms * 12 + (ms * 12 *0.05))
