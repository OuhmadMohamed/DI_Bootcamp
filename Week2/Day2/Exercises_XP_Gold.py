class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required")
        if amount <= 0:
            raise Exception("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive")
        if self.balance - amount < 0:
            raise Exception("Insufficient funds")
        self.balance -= amount

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Withdrawal would drop balance below minimum balance of {self.minimum_balance}")
        self.balance -= amount


class ATM:
    def __init__(self, account_list, try_limit):
        # Validate account_list
        if not isinstance(account_list, list) or not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("account_list must be a list of BankAccount or MinimumBalanceAccount instances")
        
        # Validate try_limit
        if not isinstance(try_limit, (int, float)) or try_limit <= 0:
            print("Invalid try_limit provided. Defaulting to 2.")
            try_limit = 2
        
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n=== ATM Main Menu ===")
            print("1. Log in")
            print("2. Exit")
            choice = input("Select an option: ").strip()
            
            if choice == "1":
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye!")
                return
            else:
                print("Invalid option. Please try again.")

    def log_in(self, username, password):
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down.")
            exit()
        
        for account in self.account_list:
            if account.authenticate(username, password):
                print("Login successful!")
                self.current_tries = 0  # Reset tries on successful login
                self.show_account_menu(account)
                return
        
        # No match found
        self.current_tries += 1
        remaining = self.try_limit - self.current_tries
        print(f"Invalid credentials. {remaining} attempt(s) remaining.")
        if remaining <= 0:
            print("Maximum login attempts reached. Shutting down.")
            exit()

    def show_account_menu(self, account):
        while True:
            print("\n=== Account Menu ===")
            print(f"Current balance: {account.balance}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Logout")
            choice = input("Select an option: ").strip()
            
            if choice == "1":
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                    print(f"Deposited {amount}. New balance: {account.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                    print(f"Withdrew {amount}. New balance: {account.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                account.authenticated = False  # Logout
                print("Logged out successfully.")
                return
            else:
                print("Invalid option. Please try again.")



#  Usage Example:
# Create some accounts
acc1 = BankAccount("user1", "pass123", balance=100)
acc2 = MinimumBalanceAccount("user2", "secret", balance=500, minimum_balance=100)

# Create ATM with accounts and try limit
atm = ATM([acc1, acc2], try_limit=3)

# The ATM will start automatically and show the main menu
