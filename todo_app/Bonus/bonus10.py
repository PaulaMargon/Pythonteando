try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("That looks like a Square")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number:")