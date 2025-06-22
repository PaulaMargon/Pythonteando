waiting_list = ["Sen","Ben","john"]
waiting_list=waiting_list.sort() #Para ordenar la lista alfabeticamente

for index, item in enumerate(waiting_list):
    row = f"{index+1}.{item.capitalize()}"