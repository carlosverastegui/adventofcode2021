def puzzle():
    with open("./files/input.txt", 'r') as file:
        nums = file.read().splitlines()
        ratings = {"oxygen": nums[:], "co2": nums[:]}

        for rating, nums in ratings.items():
            for index in range(len(nums[0])):
                pos = ["-1" if x[index] == "0" else x[index] for x in nums]
                lead = "1" if sum(map(int, pos)) >= 0 else "0"
                
                if (rating == "co2"):
                    lead = "0" if lead == "1" else "1"
                
                nums = [x for x in nums if x[index] == lead]

                if len(nums) == 1:
                    ratings[rating] = nums[0]
                    continue

    print(int(ratings["oxygen"], 2) * int(ratings["co2"], 2))    

if __name__ == "__main__":
    puzzle()