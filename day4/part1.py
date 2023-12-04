def main():
    # Read input
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    sum = 0

    for line in lines:
        [_, data] = line.strip().split(":")
        [win_num_str, my_num_str] = data.strip().split("|")

        win_num = {}
        for num in win_num_str.strip().split(" "):
            if num == "":
                continue
            win_num[int(num)] = True

        count = 0

        for num in my_num_str.strip().split(" "):
            if num == "":
                continue
            num = int(num)
            if win_num.get(num) is True:
                count += 1

        if count > 0:
            sum += 2 ** (count - 1)

    print(sum)


if __name__ == "__main__":
    main()
