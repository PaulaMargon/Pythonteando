import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input(key="file")
choose_button1 = sg.FilesBrowse("Choose File", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input(key="folder")
choose_button2 = sg.FolderBrowse("Choose Folder", key="folder")

compress_button1 = sg.Button("Compress")
output = sg.Text(key="output")

layout = [
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [compress_button1],
    [output]
]

window = sg.Window("File Compressor", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == "Compress":
        if values["files"] and values["folder"]:
            filepaths = values["files"].split(";")
            folder = values["folder"]
            make_archive(filepaths, folder)
            window["output"].update(value="Compression completed!")
        else:
            window["output"].update(value="Please select files and a folder.")
    elif event == sg.WIN_CLOSED:
        break

window.close()
