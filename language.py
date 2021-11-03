import sys
f = open(sys.argv[1], "r") #if there is a #/usr.. ,put argv[0]
Lines = f.readlines()

for line in Lines:
    text = line
    instruction = text.split(' ', 1)[0]
    if instruction == "PRINT":
        other = text.split(' ', 1)[1]
        print('"' + other + '"')
        if other == "last_input":
            print(last_input)
        else:
            string = other.replace('"', '')
            print(string)
    elif instruction == "INPUT":
        other = text.split(' ', 1)[1]

        question = other.replace('"', '')
        last_input = input(question + ' ')
f.close() 
