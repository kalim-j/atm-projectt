import os
import json

# Initialize user account with balance and PIN
account_data = {
    'pin': '1234',   # Default PIN
    'balance': 1000  # Default balance
}

# Save account information to a file
def save_account():
    with open('account.json', 'w') as file:
        json.dump(account_data, file)

# Load account information from a file
def load_account():
    if os.path.exists('account.json'):
        with open('account.json', 'r') as file:
            global account_data
            account_data = json.load(file)

# Authenticate the user with their PIN
def authenticate():
    attempts = 3
    while attempts > 0:
        pin = input("Enter your PIN: ")
        if pin == account_data['pin']:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print(f"Invalid PIN. You have {attempts} attempt(s) left.")
    print("Too many invalid attempts. Exiting.")
    return False

# View account balance
def check_balance():
    print(f"Your current balance is: ${account_data['balance']}")

# Deposit money into the account
def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        account_data['balance'] += amount
        print(f"${amount} has been deposited. New balance: ${account_data['balance']}")
        save_account()
    else:
        print("Invalid deposit amount.")

# Withdraw money from the account
def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0 and amount <= account_data['balance']:
        account_data['balance'] -= amount
        print(f"${amount} has been withdrawn. Remaining balance: ${account_data['balance']}")
        save_account()
    elif amount > account_data['balance']:
        print("Insufficient balance.")
    else:
        print("Invalid withdrawal amount.")

# Change the account PIN
def change_pin():
    current_pin = input("Enter your current PIN: ")
    if current_pin == account_data['pin']:
        new_pin = input("Enter your new PIN: ")
        confirm_pin = input("Confirm your new PIN: ")
        if new_pin == confirm_pin:
            account_data['pin'] = new_pin
            save_account()
            print("PIN successfully changed.")
        else:
            print("PINs do not match.")
    else:
        print("Incorrect current PIN.")

# ATM menu
def atm_menu():
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            change_pin()
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Main function to run the ATM system
def main():
    load_account()
    if authenticate():
        atm_menu()

if __name__ == "__main__":
    main()
