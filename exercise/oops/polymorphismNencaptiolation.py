# Custom exception for max limit exceeded
class MaxLimitExceededException(Exception):
    pass


# Bank class as a base class with withdraw method
class Bank:
    def __init__(self, max_transaction_limit, max_amount_limit):
        self.max_transaction_limit = max_transaction_limit
        self.max_amount_limit = max_amount_limit
        self.transactions_done = 0

    def withdraw(self, amount):
        pass

    def update_limits(self, amount):
        self.transactions_done += 1
        self.max_transaction_limit -= 1
        self.max_amount_limit -= amount


# HDFC Bank class extending Bank
class HDFCBank(Bank):
    def __init__(self):
        super().__init__(max_transaction_limit=3, max_amount_limit=20000)

    def withdraw(self, amount):
        if self.max_transaction_limit <= 0:
            raise MaxLimitExceededException(
                "Transaction limit exceeded for HDFC Bank")

        if self.max_amount_limit < amount:
            raise MaxLimitExceededException(
                "Amount limit exceeded for HDFC Bank")

        self.update_limits(amount)
        print(f"Withdrawn {amount} from HDFC Bank")


# AXIS Bank class extending Bank
class AXISBank(Bank):
    def __init__(self):
        super().__init__(max_transaction_limit=5, max_amount_limit=30000)

    def withdraw(self, amount):
        if self.max_transaction_limit <= 0:
            raise MaxLimitExceededException(
                "Transaction limit exceeded for AXIS Bank")

        if self.max_amount_limit < amount:
            raise MaxLimitExceededException(
                "Amount limit exceeded for AXIS Bank")

        self.update_limits(amount)
        print(f"Withdrawn {amount} from AXIS Bank")


# ATM class handling input and interactions
class ATM:
    def input_amount(self):
        continue_transaction = True
        selected_bank = None

        while continue_transaction:
            try:
                # Simulating user input for bank and amount
                # For example, taking bank_name as input from the user and amount as 100
                bank_name = input("Enter bank name (HDFC/AXIS): ")
                amount = int(input("Enter amount to withdraw: "))

                if bank_name.upper() == "HDFC":
                    selected_bank = HDFCBank()
                elif bank_name.upper() == "AXIS":
                    selected_bank = AXISBank()
                else:
                    print("Invalid Bank Name")
                    continue

                selected_bank.withdraw(amount)

                # Asking for next transaction
                next_transaction = input("Do you want to continue (yes/no): ")

                if next_transaction.lower() == "no":
                    continue_transaction = False

            except MaxLimitExceededException as e:
                print(e)
                continue_transaction = False


# Main function for execution
def main():
    atm = ATM()
    atm.input_amount()


if __name__ == "__main__":
    main()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class MaxLimitExceededError(Exception):
#     def __init__(self,message):
#         super().__init__(message)
#     pass
# class MaxTransactionLimitExceededException(Exception):
#     def __init__(self,message):
#         super().__init__(message)

# class Bank:
#     def __init__(self,Max_transaction_limit,Max_amount_limit):
#         self.Maxtransctionlimit = Max_transaction_limit
#         self.Maxamountlimit = Max_amount_limit
#         self.transctionamount = 0
#     def withdrow(self,amount):

#             if self.current_transactions >= self.max_transactions:
#                 raise MaxLimitExceededError("Max transaction limit exceeded")

#             if self.current_amount + amount > self.max_amount:
#                 raise MaxLimitExceededError("Max amount limit exceeded")

#             self.current_transactions += 1
#             self.current_amount += amount
# class HDFC(Bank):
#     def __init__(self):
#         super().__init__("HDFC Bank", max_transactions=3, max_amount=20000)

# class AXIS(Bank):
#     def __init__(self):
#         super().__init__("AXIS Bank", max_transactions=5, max_amount=30000)

# class ATM:
#     @staticmethod
#     def inputAmount():
#         bank_choice = input("Choose a bank (HDFC/AXIS): ").upper()
#         amount = int(input("Enter amount to withdraw: "))

#         if bank_choice == "HDFC":
#             bank = HDFC(Bank)
#         elif bank_choice == "AXIS":
#             bank = AXIS(Bank)
#         else:
#             print("Invalid bank choice")
#             return

    
#         try:
#             message = bank.withdraw(amount)
#             print(message)
#             print(f"Current transactions: {bank.current_transactions}/{bank.max_transactions}")
#             print(f"Current amount: {bank.current_amount}/{bank.max_amount}")

#         except MaxLimitExceededError as e:
#             print(e)
        
#         finally:
#             next_transaction = input("Do you want to perform another transaction? (yes/no): ").lower()
#             if next_transaction == "yes":
#                 ATM.inputAmount()
#             else:
#                 print("Terminating the process")

# object_atm = ATM.inputAmount()
 
    

