# Python Todo List Manager

A simple command-line todo list application with persistent storage and completion tracking.

## Features

- **Todo Management**: Create, view, complete, and delete todos
- **Persistent Storage**: Todos are automatically saved to a text file
- **Completion Tracking**: Mark todos as completed without deleting them
- **Clean Interface**: Simple menu-driven command-line interface
- **Error Handling**: Graceful handling of invalid inputs and errors

## Installation

1. Ensure you have Python 3.6 or higher installed on your system
2. Download or copy the todo manager script
3. No additional dependencies required - uses only Python standard library

## Usage

Run the todo manager program:
```bash
python todo_manager.py
```

### Menu Options

The todo manager provides the following options:

1. **View todos (1)**: Display all current todos with their numbers
2. **Add todo (2)**: Create a new todo item
3. **Complete todo (3)**: Mark a todo as completed (with or without deletion)
4. **Delete todo (4)**: Delete a specific todo item
5. **Delete completed todos (5)**: Remove all completed todos at once
6. **Show menu (6)**: Display the main menu again
7. **Save & Exit (00)**: Save all changes and exit the program

### Managing Todos

**Adding a new todo:**
1. Select option 2 from the menu
2. Enter your todo text
3. The todo will be added and saved automatically

**Marking a todo as complete:**
1. Select option 3 from the menu
2. View the list of todos and choose a number
3. Choose whether to:
   - Delete the completed todo (y)
   - Keep it in the list marked as "(completed)" (n)

**Deleting todos:**
- Use option 4 to delete specific todos
- Use option 5 to delete all completed todos at once

## How It Works

### File Structure
- `todo_manager.py` - Main todo manager program
- `todos.txt` - Auto-generated file storing todo items
- `README.md` - This documentation file

### Data Storage
Todos are stored in `todos.txt` with one todo per line:
```
Buy groceries
Finish project report (completed)
Call John
Read book (completed)
```

### Key Functions

- `save_todos()`: Saves all todos to the text file
- `load_todos()`: Loads todos from the text file on startup
- `view_todos()`: Displays all todos with numbering
- `add_todo()`: Adds a new todo to the list
- `complete_todo()`: Marks todos as completed with user choice
- `delete_todo()`: Removes specific todos
- `delete_completed_todos()`: Cleans up all completed items
- `main()`: Main program loop with menu interface

## Error Handling

The todo manager includes several error protections:
- Validates todo numbers to prevent out-of-range errors
- Handles non-numeric input gracefully
- Prevents adding empty todos
- File operations are wrapped in try-except blocks
- Handles missing data files by creating new ones

## Customization

You can modify the program by:
- Changing the data file name in `save_todos()` and `load_todos()` functions
- Adding new todo categories or priorities
- Modifying the completion marker "(completed)" to different text
- Adding due dates or reminders
- Changing the menu structure or adding new features

## Example Usage Session

```
========================================
📝 SIMPLE TODO LIST MANAGER
========================================

📝 TODO LIST MANAGER
1. View todos
2. Add todo
3. complete todo
4. delete todo
5. Delete completed todos
6. Show menu
00. Save & Exit

👉 Enter choice (1-6 / 00): 2

✏️ Enter new todo: Buy milk
✅ Added: Buy milk

👉 Enter choice (1-6 / 00): 1

📋 YOUR TODOS:
1. Buy milk

👉 Enter choice (1-6 / 00): 3

📋 YOUR TODOS:
1. Buy milk

✅ Enter todo number to mark complete: 1
Are you want to delete this todo? (y/n): n
✅ Marked as complete: Buy milk (completed)
```

## Limitations

- Command-line interface only (no GUI)
- Basic text-based storage (no database)
- No sorting or filtering capabilities
- No due dates or priority levels
- No search functionality

## Future Enhancements

Potential improvements could include:
- Due dates and reminders
- Priority levels (high, medium, low)
- Categories or tags for todos
- Search and filter functionality
- Export todos to different formats (CSV, JSON)
- Undo/redo functionality
- Graphical user interface (GUI)
- Cloud synchronization
- Recurring todos
- Todo statistics and progress tracking

## License

This project is open source and available for educational and personal use.

## Author

Created as a Python learning project to demonstrate file handling, list manipulation, and user interface design.

## Contributing

Feel free to fork this project and submit pull requests with improvements or additional features. Suggestions for new features or bug reports are welcome through GitHub issues.