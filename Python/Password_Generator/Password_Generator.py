def show_menu():
    print("1. generate new password")
    print("2. show saved password")
    print("3. delete a saved password")
    print("4. delete all saved password")
    print("00. exit tool")

def load_password():
    try:
        with open("password_history.txt", 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []

def show_password(passwords):
    if not passwords:
        print("\n📭 No passwords found1")
        return
    
    print("\n Your Passwords:")
    for i, password in enumerate(passwords, 1):
        print(f"{i}. {password}")

def delete_password(passwords):
    if passwords:
        try:
            num = int(input("\nEnter password number to delete: "))
            if 1 <= num <= len(passwords):
                deleted = passwords.pop(num - 1)
                print(f"Deleted {deleted}")
            else:
                print("Invalid Number!")
        except ValueError:
            print("Please enter a vaavid number")

def delete_all_passwords(passwords):
    if passwords:
        with open("password_history.txt", 'w') as file:
            file.write("")

def add_new_password(new_password):
    with open("password_history.txt", 'a') as file:
        file.write(new_password + "\n")

def generate_password():
    import string
    import secrets
    try:
        length = int(input("\nEnter password length (3-20): "))
        if not (3 <= length <= 20):
            print("Error: Length must be between 3 and 20.")
            return
        
        # Define character sets
        nums = string.digits
        alpha = string.ascii_letters
        special = string.punctuation

        # Map choices to combined character pools
        options = {
            1: nums,
            2: alpha,
            3: special,
            4: nums + alpha,
            5: alpha + special,
            6: nums + special,
            7: nums + alpha + special
        }

        print("(1) -> Number Only\n(2) -> Alphabet Only\n(3) -> Special Character Only\n(4) -> Number+Alphabet\n(5) -> Alphabet+special Char\n(6) -> Number+Special Char\n(7) -> All Mix")
        choice = int(input("Choose a Number (1-7): "))
        
        # Validate choice and generate
        if choice in options:
            char_pool = options[choice]
            # secrets.choice is more secure than random.choice
            password = ''.join(secrets.choice(char_pool) for _ in range(length))
            
            print(f"\nYour generated password: {password}")

            conformation = input("Do you want to save this password? (y/n): ").lower()
            if conformation == 'n':
                print("Password not saved.")
            else:
                add_new_password(password)
                print("Password saved successfully!")

        else:
            print("Invalid choice! Please select 1-7.")

    except ValueError:
        print("Invalid input! Please enter numerical values.")

def main():
    print("=" * 40)
    print("simple password generator")
    print("=" * 40)
    show_menu()

    passwords = load_password()

    while True:
        try:
            choice = int(input("\nEnter choice (1-5 / 00): "))

            if choice == 1:
                generate_password()
            elif choice == 2:
                show_password(passwords)
            elif choice == 3:
                delete_password(passwords)
            elif choice == 4:
                delete_all_passwords(passwords)
            elif choice == 5:
                show_menu()
            elif choice == 00:
                print("\nThanks for using. Good bye!")
                break
        except ValueError:
            print("Please enter a number")
        except KeyboardInterrupt:
            print("exiting...")
            break

if __name__ == "__main__":
    main()