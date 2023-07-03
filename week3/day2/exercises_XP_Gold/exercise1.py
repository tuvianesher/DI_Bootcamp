class BankAccount:
    def __init__(self):
        self.balance = 0
        self.username = ""
        self.password = ""
        self.authenticated = False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You are not authenticated to perform this action.")
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive integer.")
        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You are not authenticated to perform this action.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be a positive integer.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance=0):
        super().__init__()
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You are not authenticated to perform this action.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be a positive integer.")
        if self.balance - amount < self.minimum_balance:
            raise ValueError("Withdrawal amount exceeds allowed balance.")
        self.balance -= amount


class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list) or not all(
            isinstance(account, (BankAccount, MinimumBalanceAccount)) for account in account_list
        ):
            raise ValueError(
                "Invalid input for account_list. It should be a list of BankAccount or MinimumBalanceAccount instances."
            )
        if try_limit <= 0:
            raise ValueError("try_limit must be a positive number.")
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

    def show_main_menu(self):
        while True:
            print("ATM Main Menu")
            print("1. Log in")
            print("2. Exit")

            choice = input("Enter your choice (1-2): ")
            if choice == "1":
                self.log_in()
            elif choice == "2":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def log_in(self):
        while self.current_tries < self.try_limit:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for account in self.account_list:
                account.authenticate(username, password)
                if account.authenticated:
                    self.show_account_menu(account)
                    return

            self.current_tries += 1
            print("Invalid username or password. Please try again.")

        print("You have reached the maximum number of tries. The ATM will shut down.")

    def show_account_menu(self, account):
        while True:
            print("\nAccount Menu")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ")
            if choice == "1":
                amount = int(input("Enter the amount to deposit: "))
                try:
                    account.deposit(amount)
                    print("Deposit successful.")
                except Exception as e:
                    print(str(e))
            elif choice == "2":
                amount = int(input("Enter the amount to withdraw: "))
                try:
                    account.withdraw(amount)
                    print("Withdrawal successful.")
                except Exception as e:
                    print(str(e))
            elif choice == "3":
                print("Returning to main menu.")
                break
            else:
                print("Invalid choice. Please try again.")


# Example usage:

# Create BankAccount and MinimumBalanceAccount instances
account1 = BankAccount()
account1.username = "user1"
account1.password = "pass1"

account2 = MinimumBalanceAccount(minimum_balance=100)
account2.username = "user2"
account2.password = "pass2"

# Create ATM instance
account_list = [account1, account2]
try_limit = 3
atm = ATM(account_list, try_limit)

# Start ATM program
atm.show_main_menu()
