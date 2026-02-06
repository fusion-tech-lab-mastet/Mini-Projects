def show_menu():
    print("\n📝 TODO LIST MANAGER")
    print("1. View todos")
    print("2. Add todo")
    print("3. complete todo")
    print("4. delete todo")
    print("00. Save & Exit")

def save_todos(todos):
    with open("todos.txt", "w") as file:
        for todo in todos:
            file.write(todo + "\n")

def load_todos():
    try:
        with open("todos.txt", "r") as file:
            todos = file.read().splitlines()
        return [todo for todo in todos if todo]  # Remove empty lines
    except FileNotFoundError:
        return []

def view_todos(todos):
    if not todos:
        print("\n📭 No todos found!")
        return
    
    print("\n📋 YOUR TODOS:")
    for i, todo in enumerate(todos, 1):
        print(f"{i}. {todo}")

def add_todo(todos):
    task = input("\n✏️ Enter new todo: ").strip()
    if task:
        todos.append(task)
        print(f"✅ Added: {task}")
    else:
        print("❌ Cannot add empty todo!")

def complete_todo(todos):
    view_todos(todos)
    if todos:
        try:
            num = int(input("\n✅ Enter todo number to mark complete: "))
            choice = input("Are you want to delete this todo? (y/n): ").strip().lower()
            if choice == 'y':
                if 1 <= num <= len(todos):
                    completed = todos.pop(num - 1)
                    print(f"🎉 Completed: {completed}")
                else:
                    print("❌ Invalid number!")
            elif choice == 'n':
                if 1 <= num <= len(todos):
                    print(f"✅ Marked as complete: {todos[num - 1]}")
                    todos[num - 1] = todos[num - 1] + " (completed)"
                else:
                    print("❌ Something went wrong!")
        except ValueError:
            print("❌ Please enter a valid number!")

def delete_completed_todos(todos):
    completed_todos = [todo for todo in todos if todo.endswith("(completed)")]
    if not completed_todos:
        print("\n📭 No completed todos in the list!")
        return
    print("\n🗑️ COMPLETED TODOS:")
    for i, todo in enumerate(completed_todos, 1):
        print(f"{i}. {todo}")
    
    for todo in completed_todos:
        todos.remove(todo)

def delete_todo(todos):
    view_todos(todos)
    if todos:
        try:
            num = int(input("\n🗑️ Enter todo number to delete: "))
            if 1 <= num <= len(todos):
                deleted = todos.pop(num - 1)
                print(f"🗑️ Deleted: {deleted}")
            else:
                print("❌ Invalid number!")
        except ValueError:
            print("❌ Please enter a valid number!")

def main():
    print("=" * 40)
    print("📝 SIMPLE TODO LIST MANAGER")
    print("=" * 40)
    show_menu()
    
    todos = load_todos()
    
    while True:
        
        try:
            choice = int(input("\n👉 Enter choice (1-6 / 00): "))
            
            if choice == 1:
                view_todos(todos)
            elif choice == 2:
                add_todo(todos)
            elif choice == 3:
                complete_todo(todos)
            elif choice == 4:
                delete_todo(todos)
            elif choice == 5:
                delete_completed_todos(todos)
            elif choice == 6:
                show_menu()
            elif choice == 00:
                save_todos(todos)
                print("\n💾 Saved todos to file!")
                print("👋 Goodbye!")
                break
            else:
                print("❌ Please choose 1-5 only!")
                
        except ValueError:
            print("❌ Please enter a number!")
        except KeyboardInterrupt:
            print("\n\n⚠️ Saving and exiting...")
            save_todos(todos)
            break

if __name__ == "__main__":
    main()