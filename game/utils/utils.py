def input_integer(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Please enter a number")