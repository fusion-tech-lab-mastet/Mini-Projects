# Python Calculator with History

A simple command-line calculator with session-based calculation history tracking.

## Features

- **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Session Management**: Organizes calculations into separate sessions
- **History Tracking**: Automatically saves all calculations to a text file
- **History Management**: View, clear, or create new sessions at any time
- **Persistent Storage**: Calculations are saved between program runs
- **Error Handling**: Handles division by zero and invalid operators gracefully

## Installation

1. Ensure you have Python 3.6 or higher installed on your system
2. Download or clone the repository
3. No additional dependencies required - uses only Python standard library

## Usage

Run the calculator program:
```bash
python calculator.py
```

### Menu Options

The calculator provides the following options:

1. **Simple Calculator (00 or any key)**: Perform arithmetic calculations
2. **Exit (0)**: Quit the program
3. **Clear History (1)**: Delete all calculation history
4. **Show History (2)**: Display all saved calculations
5. **Create new session (3)**: Start a fresh session without clearing history

### Performing Calculations

When using the simple calculator:
1. Enter the first number
2. Choose an operator (+, -, *, /)
3. Enter the second number
4. View the result

The calculation will automatically be saved to the history.

## How It Works

### File Structure
- `calculator.py` - Main calculator program
- `calculator_history.txt` - Auto-generated file storing calculation history
- `README.md` - This documentation file

### History Storage
Calculations are stored in `calculator_history.txt` with the following format:
```
=== New Session Started ===
Calculation Number '1' => 10.0 + 5.0 = 15.0
Calculation Number '2' => 20.0 * 3.0 = 60.0
=== New Session Started ===
Calculation Number '1' => 15.0 - 7.0 = 8.0
```

### Key Functions

- `save_history()`: Appends calculations to the history file
- `show_history()`: Reads and displays all saved calculations
- `create_session()`: Adds session separator to the history
- `clear_history()`: Clears all calculation history
- `main()`: Main program loop with menu interface

## Error Handling

The calculator includes several error protections:
- Prevents division by zero
- Validates operator input (only +, -, *, / allowed)
- Handles non-numeric input gracefully
- File operations are wrapped in try-except blocks

## Customization

You can modify the program by:
- Changing the history file name in the `save_history()` function
- Adding new mathematical operations
- Modifying the history format
- Changing session separator text in `create_session()`

## Example Usage Session

```
Welcome to the Python Calculator!

Select an operation:
00. Simple Calculator
0. Exit
1. Clear History
2. Show History
3. Create new session
Enter your choice (0, 1, 2, enter anything): 
Enter the first number: 10
Enter the operator (+, -, *, /): +
Enter the second number: 5
The result of 10.0 + 5.0 is: 15.0
```

## Limitations

- Only supports basic arithmetic operations
- Command-line interface only (no GUI)
- History is stored in plain text format
- No advanced mathematical functions

## Future Enhancements

Potential improvements could include:
- Advanced mathematical operations (power, square root, etc.)
- Support for parentheses and complex expressions
- Graphical user interface (GUI)
- Export history to different formats (CSV, JSON)
- Undo/redo functionality
- Calculation statistics and analytics

## License

This project is open source and available for educational and personal use.

## Author

Created as a Python learning project to demonstrate file handling, user input processing, and basic program structure.

## Contributing

Feel free to fork this project and submit pull requests with improvements or additional features.