while True:
    text = input("bpl > ")
    instruction = text.split(' ', 1)[0]
    if text == "exit":
        break
    elif instruction == "PRINT":
        other = text.split(' ', 1)[1]
        string = other.replace('"', '')
        print(string)
    elif instruction == "INPUT":
        other = text.split(' ', 1)[1]
        question = other.replace('"', '')
        input(question + ' ')
    else:
        print(text)
