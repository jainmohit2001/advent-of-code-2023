from typing import List


class Record:
    red: int
    green: int
    blue: int

    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
        self.red = red
        self.green = green
        self.blue = blue


class Game:
    def __init__(self, id: int, record_list: List[Record]):
        self.id = id
        self.record_list = record_list


def parse_games(lines: List[str]) -> List[Game]:
    games: List[Game] = []

    for line in lines:
        line = line.strip()
        [game, records_str] = line.split(":")
        [_, game_id_str] = game.split(" ")

        record_str_list = records_str.strip().split(";")
        record_list: List[Record] = []

        for record_str in record_str_list:
            items = record_str.strip().split(",")

            record = Record()
            for item in items:
                [num, color] = item.strip().split(" ")
                if color == "red":
                    record.red = int(num)
                elif color == "green":
                    record.green = int(num)
                elif color == "blue":
                    record.blue = int(num)

            record_list.append(record)

        games.append(Game(int(game_id_str), record_list))

    return games
