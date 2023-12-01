def main():
    # Read input
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    total = 0

    for line in lines:
        first_digit = None
        last_digit = None
        line_length = len(line)

        # Find the first digit from the start of the line
        for i in range(line_length):
            char = line[i]
            if char >= '0' and char <= '9':
                first_digit = char
                break

        # Find the first digit from the end of the line
        for i in range(len(line) - 1, -1, -1):
            char = line[i]
            if char >= '0' and char <= '9':
                last_digit = char
                break
        
        total += int(first_digit + last_digit)
    
    print(total)


if __name__ == "__main__":
    main()