from modules import functions
import time

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    # if "add" in user_action in user_action:
    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos, "todos.txt")

    elif user_action.startswith('show'):
        todos = functions.get_todos('todos.txt')
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo:")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, "todos.txt")
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, "todos.txt")
            message = f"Todo {todo_to_remove} has been completed."
            print(message)
        except IndexError:
            print("There is no item with that number")

    elif 'exit' in user_action:
        break
    else:
        print("Invalid input")
