def puzzle():
    num_larger = -1
    prev_measure = 0

    with open("./files/input.txt", 'r') as file:
        for line in file:
            cur_measure = int(line)

            if (prev_measure < cur_measure):
                num_larger += 1

            prev_measure = cur_measure

    print(num_larger)

if __name__ == "__main__":
    puzzle()