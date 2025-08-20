# import datetime
# class BankAccount:
#     def __init__(self, account_number, holder_name, balance=0):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = balance
#         self.transactions = []  

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self.transactions.append(
#                 (datetime.datetime.now(), f"Deposited: {amount}", self.balance)
#             )
#             print(f"Deposited {amount}. Current Balance: {self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if self.balance >= amount:
#                 self.balance -= amount
#                 self.transactions.append(
#                     (datetime.datetime.now(), f"Withdrew: {amount}", self.balance)
#                 )
#                 print(f"Withdrawn {amount}. Current Balance: {self.balance}")
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Withdrawal amount must be positive.")

#     def show_balance(self):
#         print(f"Current Balance: {self.balance}")

#     def show_transactions(self):
#         if not self.transactions:
#             print("No transactions yet.")
#         else:
#             print("\nTransaction History:")
#             for t in self.transactions:
#                 print(f"{t[0].strftime('%Y-%m-%d %H:%M:%S')} | {t[1]} | Balance: {t[2]}")


# # Menu-driven app
# def main():
#     print("Welcome to Simple Banking System")
#     account = BankAccount(account_number="123456", holder_name="Riddhi", balance=1000)

#     while True:
#         print("\n====== MENU ======")
#         print("1. Deposit Money")
#         print("2. Withdraw Money")
#         print("3. Show Balance")
#         print("4. Transaction History")
#         print("5. Exit")
        
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             amount = float(input("Enter deposit amount: "))
#             account.deposit(amount)

#         elif choice == "2":
#             amount = float(input("Enter withdrawal amount: "))
#             account.withdraw(amount)

#         elif choice == "3":
#             account.show_balance()

#         elif choice == "4":
#             account.show_transactions()

#         elif choice == "5":
#             print("Thank you for banking with us!")
#             break

#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()


import datetime
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []   
        print("Welcome to the Machine")

    # def deposit(self):
    #     try:
    #         amount = float(input("Enter amount to be Deposited: "))
    #         if amount > 0:
    #             self.balance += amount
    #             self.transactions.append(
    #                 (datetime.datetime.now(), f"Deposited: {amount}", self.balance)
    #             )
    #             print("\nAmount Deposited:", amount)
    #         else:
    #             print("Deposit amount must be positive.")
    #     except ValueError:
    #         print("Invalid input! Please enter a number.")

    # def withdraw(self):
    #     try:
    #         amount = float(input("Enter amount to be withdrawn: "))
    #         if amount > 0:
    #             if self.balance >= amount:
    #                 self.balance -= amount
    #                 self.transactions.append(
    #                     (datetime.datetime.now(), f"Withdrew: {amount}", self.balance)
    #                 )
    #                 print("\nYou withdrew:", amount)
    #             else:
    #                 print("\nInsufficient balance")
    #         else:
    #             print("Withdrawal amount must be positive.")
    #     except ValueError:
    #         print("Invalid input! Please enter a number.")
    
    def deposit(self):
        while True:
            amount = input("Enter amount to be Deposited: ").strip()
            if amount.replace('.', '', 1).isdigit():  # check if number (allows decimals)
                amount = float(amount)
                if amount > 0:
                    self.balance += amount
                    self.transactions.append(
                        (datetime.datetime.now(), f"Deposited: {amount}", self.balance)
                    )
                    print("\nAmount Deposited:", amount)
                    break
                else:
                    print("Deposit amount must be positive.")
            else:
                print("Invalid input! Please enter a valid number.")


    def withdraw(self):
        while True:
            amount = input("Enter amount to be Withdrawn: ").strip()
            if amount.replace('.', '', 1).isdigit():  # check if number (allows decimals)
                amount = float(amount)
                if amount > 0:
                    if self.balance >= amount:
                        self.balance -= amount
                        self.transactions.append(
                            (datetime.datetime.now(), f"Withdrew: {amount}", self.balance)
                        )
                        print("\nYou withdrew:", amount)
                        break
                    else:
                        print("Insufficient balance.")
                        break
                else:
                    print("Withdrawal amount must be positive.")
            else:
                print("Invalid input! Please enter a valid number.")


    def show_transactions(self):
        if not self.transactions:
            print("\nNo transactions yet.")
        else:
            print("\nTransaction History:")
            for t in self.transactions:
                print(f"{t[0].strftime('%Y-%m-%d %H:%M:%S')} | {t[1]} | Balance: {t[2]}")
        
    def display(self):
        print("\nNet Available Balance =", self.balance)

if __name__ == "__main__":
    s = BankAccount()       # create an object of BankAccount
    s.deposit()             # deposit money 
    s.withdraw()            # withdraw money  
    s.show_transactions()   # show transaction history  
    s.display()             # display balance
    
