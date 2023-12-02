from utils import parse_games, Game


def is_valid_game(
    game: Game, red_limit: int, green_limit: int, blue_limit: int
) -> bool:
    for record in game.record_list:
        if (
            record.red > red_limit
            or record.green > green_limit
            or record.blue > blue_limit
        ):
            return False

    return True


def main():
    # Read input
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    red_limit = 12
    green_limit = 13
    blue_limit = 14

    sum = 0

    games = parse_games(lines)
    for game in games:
        if is_valid_game(game, red_limit, green_limit, blue_limit):
            sum += game.id

    print(sum)


if __name__ == "__main__":
    main()
