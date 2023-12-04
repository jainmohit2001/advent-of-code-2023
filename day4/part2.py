def main():
    # Read input
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    card_count = {}

    for line in lines:
        [card, data] = line.strip().split(":")
        card_id = int(card[4:])

        if card_id in card_count:
            card_count[card_id] += 1
        else:
            card_count[card_id] = 1

        current_card_count = card_count[card_id]

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
            for i in range(card_id + 1, card_id + 1 + count):
                if i in card_count:
                    card_count[i] += 1 * current_card_count
                else:
                    card_count[i] = 1 * current_card_count

    total_cards = 0
    for count in card_count.values():
        total_cards += count

    print(total_cards)


if __name__ == "__main__":
    main()
