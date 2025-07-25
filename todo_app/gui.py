from modules import functions
import FreeSimpleGUI as sg

from modules import functions
import FreeSimpleGUI as sg
import time

sg.theme('Black')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=3, mouseover_colors=("lightBlue2"))
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'].strip() + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            if values['todos']:  # Solo si hay selección
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].strip() + "\n"
                todos = functions.get_todos()
                # Normalizar para comparar correctamente
                todos_normalizados = [t.strip() for t in todos]
                try:
                    index = todos_normalizados.index(todo_to_edit.strip())
                    todos[index] = new_todo
                    functions.write_todos(todos)
                    window["todos"].update(values=todos)
                except ValueError:
                    pass  # No encontró el elemento, no hace nada
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos":
            if values['todos']:
                window["todo"].update(value=values['todos'][0].strip())
        case sg.WIN_CLOSED:
            break

window.close()

window.close()
