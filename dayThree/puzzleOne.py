def puzzle():
    gamma, epsilon = "", ""

    with open("./files/input.txt", 'r') as file:
        nums = file.read().splitlines()
        
        for index in range(len(nums[0])):
            pos = ["-1" if x[index] == "0" else x[index] for x in nums]
            majority = "1" if sum(map(int, pos)) >= 0 else "0"
            
            gamma += majority
            epsilon += "0" if majority == "1" else "1"

    print(int(gamma, 2) * int(epsilon, 2))

if __name__ == "__main__":
    puzzle()