# Python Password Generator

A secure command-line password generator with history tracking and management features.

## Features

- **Secure Password Generation**: Creates strong, random passwords using Python's `secrets` module
- **Customizable Options**: 7 different character combination options (numbers, letters, special characters, or any mix)
- **Adjustable Length**: Generate passwords between 3-20 characters
- **Password History**: Automatically saves generated passwords to a text file
- **History Management**: View, delete individual passwords, or clear all saved passwords
- **Persistent Storage**: Passwords are saved between program runs
- **Error Handling**: Graceful handling of invalid inputs and file operations

## Installation

1. Ensure you have Python 3.6 or higher installed on your system
2. Download or copy the password generator script
3. No additional dependencies required - uses only Python standard library

## Usage

Run the password generator program:
```bash
python Password_Generator.py
```

### Menu Options

The password generator provides the following options:

1. **Generate new password (1)**: Create a new password with custom settings
2. **Show saved passwords (2)**: Display all previously saved passwords
3. **Delete a saved password (3)**: Remove a specific password from history
4. **Delete all saved passwords (4)**: Clear the entire password history
5. **Show menu (5)**: Display the main menu again
6. **Exit tool (00)**: Quit the program

### Generating a Password

When generating a new password:
1. Enter desired password length (3-20 characters)
2. Choose a character combination type (1-7):
   - (1) Numbers Only
   - (2) Alphabet Only
   - (3) Special Characters Only
   - (4) Numbers + Alphabet
   - (5) Alphabet + Special Characters
   - (6) Numbers + Special Characters
   - (7) All Mix (Numbers + Alphabet + Special Characters)
3. View your generated password
4. Choose whether to save it to history (y/n)

## How It Works

### File Structure
- `Password_Generator.py` - Main password generator program
- `password_history.txt` - Auto-generated file storing saved passwords
- `README.md` - This documentation file

### Password Storage
Passwords are stored in `password_history.txt` with one password per line:
```
kL9$mN2@pQ5&rS7
Xy3#wR8*tU1%vB6
Jh4^fG7!cV2@dN5
```

### Key Functions

- `generate_password()`: Creates secure random passwords using `secrets.choice()`
- `add_new_password()`: Appends generated passwords to history file
- `load_password()`: Loads saved passwords from file on startup
- `show_password()`: Displays all saved passwords with numbering
- `delete_password()`: Removes specific passwords from history
- `delete_all_passwords()`: Clears entire password history
- `show_menu()`: Displays the main menu interface
- `main()`: Main program loop with menu handling

## Security Features

The password generator prioritizes security through:
- **Cryptographically Secure Generation**: Uses `secrets` module instead of `random` for unpredictable passwords
- **Local Storage Only**: Passwords are saved locally on your device
- **No Network Access**: Completely offline operation
- **User Control**: Full control over which passwords to save or delete

## Error Handling

The password generator includes several error protections:
- Validates password length (must be between 3-20 characters)
- Ensures character combination choice is valid (1-7)
- Handles non-numeric input gracefully
- Prevents invalid password numbers when deleting
- File operations are wrapped in try-except blocks
- Handles missing history files by creating new ones
- Keyboard interrupt (Ctrl+C) support for clean exit

## Customization

You can modify the program by:
- Changing the history file name in file operation functions
- Adjusting the minimum and maximum password length limits
- Adding new character combination options
- Modifying the character sets (e.g., exclude confusing characters like O/0, l/1)
- Changing the password history format
- Adding password strength indicators

## Example Usage Session

```
========================================
simple password generator
========================================
1. generate new password
2. show saved password
3. delete a saved password
4. delete all saved password
00. exit tool

Enter choice (1-5 / 00): 1

Enter password length (3-20): 12
(1) -> Number Only
(2) -> Alphabet Only
(3) -> Special Character Only
(4) -> Number+Alphabet
(5) -> Alphabet+special Char
(6) -> Number+Special Char
(7) -> All Mix
Choose a Number (1-7): 7

Your generated password: aR7$kL2#nP9@qM5
Do you want to save this password? (y/n): y
Password saved successfully!

Enter choice (1-5 / 00): 2

 Your Passwords:
1. aR7$kL2#nP9@qM5
```

## Limitations

- Command-line interface only (no GUI)
- Basic text-based storage (no encryption for saved passwords)
- No password strength indicators
- No categorization or tags for different passwords
- No search functionality
- Passwords are stored in plain text (consider this for sensitive use)

## Future Enhancements

Potential improvements could include:
- **Password Encryption**: Encrypt saved passwords with a master password
- **Strength Meter**: Display password strength during generation
- **Copy to Clipboard**: Automatically copy generated passwords
- **Password Categories**: Organize passwords by purpose (email, banking, social media)
- **Export Options**: Export passwords to CSV or encrypted formats
- **Password Expiry**: Track and notify about old passwords
- **Pronounceable Passwords**: Generate memorable but secure passwords
- **Two-Factor Authentication**: Add 2FA code generation
- **Password Analysis**: Check for weak or repeated passwords
- **GUI Interface**: Graphical user interface for easier use

## License

This project is open source and available for educational and personal use.

## Author

Created as a Python learning project to demonstrate secure random generation, file handling, and user input processing.

## Contributing

Feel free to fork this project and submit pull requests with improvements or additional features. Suggestions for new features or bug reports are welcome through GitHub issues.