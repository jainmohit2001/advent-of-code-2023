def is_star(char: str) -> bool:
    return char == "*"


def main():
    # Read file
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    new_line_length = len(lines[0]) + 2

    # Add empty box with '.' character around the input
    empty_line = "." * new_line_length
    lines.insert(0, empty_line)
    lines.append(empty_line)
    for i in range(1, len(lines) - 1):
        lines[i] = "." + lines[i].strip() + "."

    # Stores the number around a given location of '*' symbol
    store = {}

    for i in range(1, len(lines) - 1):
        j = 1
        while j < new_line_length - 1:
            if lines[i][j] == "." or lines[i][j] < "0" or lines[i][j] > "9":
                j += 1
                continue

            # Parse the number first
            start_pos = j
            while j < new_line_length - 1 and lines[i][j] >= "0" and lines[i][j] <= "9":
                j += 1
            num = lines[i][start_pos:j]

            is_valid = False
            symbol: str = None

            # Check if there exists any '*' symbol around the number
            for j1 in range(start_pos - 1, j + 1):
                if is_star(lines[i - 1][j1]):
                    is_valid = True
                    symbol = f"{i - 1}-{j1}"
                    break

                if is_star(lines[i + 1][j1]):
                    symbol = f"{i + 1}-{j1}"
                    is_valid = True
                    break

            if is_star(lines[i][start_pos - 1]):
                symbol = f"{i}-{start_pos - 1}"
                is_valid = True

            if not is_valid and is_star(lines[i][j]):
                symbol = f"{i}-{j}"
                is_valid = True

            if is_valid:
                if symbol in store:
                    store[symbol].append(int(num))
                else:
                    store[symbol] = [int(num)]

    sum = 0

    for arr in store.values():
        if len(arr) == 2:
            sum += arr[0] * arr[1]

    print(sum)


if __name__ == "__main__":
    main()
