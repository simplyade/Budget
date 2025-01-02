#BudgetApp
'''
Create a Budget class that can instantiate objects based on different budget
categories like food, clothing, and entertainment. These objects should allow for
1. Depositing funds to each of the categories
2. Withdrawing funds from each category
3. Computing category balances
4. Transferring balance amounts between categories
Push your code to GitHub, and submit the repo link.

	


class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.amount += amount
        return f"Deposited {amount} into {self.category}"

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.amount:
            raise ValueError("Insufficient balance")
        self.amount -= amount
        return f"Withdrew {amount} from {self.category}"

    def transfer_to(self, other_budget, amount):
        if amount < 0:
            raise ValueError("Transfer amount cannot be negative")
        if amount > self.amount:
            raise ValueError("Insufficient balance")
        self.amount -= amount
        other_budget.amount += amount
        return f"Transferred {amount} from {self.category} to {other_budget.category}"

    def get_balance(self):
        return self.amount

Example usage
food = Budget("Food", 40000)
print(food.deposit(300))
print(food.transfer_to(Budget("Entertainment", 0), 30000))
print(food.get_balance())
               



    
          



     


         
     
          


         
         
