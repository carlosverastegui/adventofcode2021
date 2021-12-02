def puzzle():
    position = 0
    depth = 0

    with open("./files/input.txt", 'r') as file:
        for line in file:
            command, num = line.split()

            if command == "forward":
                position += int(num)
            elif command == "up":
                depth -= int(num)
            elif command == "down":
                depth += int(num)

    print(position * depth)

if __name__ == "__main__":
    puzzle()