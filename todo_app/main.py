def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit or exit:")
    user_action = user_action.strip()

    # if "add" in user_action in user_action:
    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos('todos.txt')
        todos.append(todo + '\n')
        write_todos('todos.txt', todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos('todos.txt')

            new_todo = input("Enter a new todo:")
            todos[number] = new_todo + '\n'

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos('todos.txt')
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} has been completed."
            print(message)
        except IndexError:
            print("There is no item with that number")

    elif 'exit' in user_action:
        break
    else:
        print("Invalid input")
