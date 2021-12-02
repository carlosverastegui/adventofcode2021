def puzzle():
    num_larger = -1
    prev_sum = 0
    window = []

    with open("./files/input.txt", 'r') as file:
        for line in file:
            cur_measure = int(line)
            window.append(cur_measure)

            if (len(window) == 3):
                cur_sum = sum(window)

                if (prev_sum < cur_sum):
                    num_larger += 1

                prev_sum = cur_sum
                window.pop(0)

    print(num_larger)

if __name__ == "__main__":
    puzzle()