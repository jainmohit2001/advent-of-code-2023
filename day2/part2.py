from utils import Game, parse_games


def find_power(game: Game):
    red = 0
    green = 0
    blue = 0
    for record in game.record_list:
        red = max(red, record.red)
        green = max(green, record.green)
        blue = max(blue, record.blue)

    return red * green * blue


def main():
    # Read input
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    games = parse_games(lines)

    sum = 0

    for game in games:
        sum += find_power(game)

    print(sum)


if __name__ == "__main__":
    main()
