def check_spelled_num(i: int, line: str) -> str:
    three_char = line[i:i+3]
    four_char = line[i:i+4]
    five_char = line[i:i+5]

    if three_char == 'one':
        return '1'
    if three_char == 'two':
        return '2'
    if five_char == 'three':
        return '3'
    if four_char == 'four':
        return '4'
    if four_char == 'five':
        return '5'
    if three_char == 'six':
        return '6'
    if five_char == 'seven':
        return '7'
    if five_char == 'eight':
        return '8'
    if four_char == 'nine':
        return '9'
    
    return None
    


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
            
            # Check for each number spelled out as string
            num = check_spelled_num(i, line)
            if num is not None:
                first_digit = num
                break

        # Find the first digit from the end of the line
        for i in range(len(line) - 1, -1, -1):
            char = line[i]
            if char >= '0' and char <= '9':
                last_digit = char
                break
                
            # Check for each number spelled out as string
            num = check_spelled_num(i, line)
            if num is not None:
                last_digit = num
                break
        
        total += int(first_digit + last_digit)
    
    print(total)


if __name__ == "__main__":
    main()