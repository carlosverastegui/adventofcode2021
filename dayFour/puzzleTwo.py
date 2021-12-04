class Crossword:
    def __init__(self, rows):
        numbered = [list(map(int, x.split())) for x in rows]
        tupled = [[(y, 0) for y in x] for x in numbered]

        self.rows = tupled

    def mark(self, num):
        self.rows = [[(y[0], 1) if y[0] == num else y for y in x] \
                    for x in self.rows]

        return self.check_bingo()

    def check_bingo(self):
        row_sums = [sum([y[1] for y in x]) for x in self.rows]
        col_sums = [sum([y[x][1] for y in self.rows]) for x in range(5)]

        return sum([sum([y[0] for y in x if y[1] == 0]) for x in self.rows]) \
            if (5 in row_sums) or (5 in col_sums) \
                else 0

def create_boards(data):
    numbers = list(map(int, data[0].split(",")))
    data = [x for x in data[2:] if x != ""]

    boards = [Crossword(data[i:i+5]) for i in range(0, len(data), 5)]
    return numbers, boards

def puzzle():
    with open("./files/input.txt", "r") as file:
        data = file.read().splitlines()

        numbers, boards = create_boards(data)
        last_score = 0

        for number in numbers:
            for board in boards[:]:
                score = board.mark(number)

                if score != 0:
                    last_score = number * score
                    boards.remove(board)

        print(last_score)

if __name__ == "__main__":
    puzzle()