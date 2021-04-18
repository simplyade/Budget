#BudgetApp
'''
Create a Budget class that can instantiate objects based on different budget
categories like food, clothing, and entertainment. These objects should allow for
1. Depositing funds to each of the categories
2. Withdrawing funds from each category
3. Computing category balances
4. Transferring balance amounts between categories
Push your code to GitHub, and submit the repo link.

	
'''

class Budget:  #can be any amount or integer input
     def __init__(self,category,amount):
          self.category=category
          self.amount = amount
          
          
     def deposit (self,pay):
          self.pay=pay
          self.amount=int((self.amount) + (self.pay))
          return 'You deposited {}'.format(self.amount)


     def transfer (self,transfer_amt):
          self.transfer_amt=transfer_amt
          if self.amount>= transfer_amt:
               return 'You transfered {}'.format(self.transfer_amt)
          else:
               return "Invalid Transfer"

     def balance(self,transfer_amt):
          self.transfer_amt=transfer_amt
          if self.amount>= transfer_amt:
               self.amount-=transfer_amt
               return "Your balance is {}:".format(int(self.amount)-(self.transfer_amt))
     
               
food = Budget("Food",40000)
print(food.deposit(300))
print(food.transfer(30000))
#print(food)



    
          



     


         
     
          


         
         
