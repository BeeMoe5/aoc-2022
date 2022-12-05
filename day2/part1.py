def main():
    with open("input.txt", "r") as file:
        inputs_str = file.read()

    points = 0

    translated = translate_input(inputs_str)
    splitted_translated = translated.splitlines()

    for players in splitted_translated:
        p2_hand, p1_hand = players.split()

        if p1_hand == p2_hand:
            # tie, give 3 points
            points += 3
        elif (
            (p1_hand == "rock" and p2_hand == "scissors")
            or (p1_hand == "paper" and p2_hand == "rock")
            or (p1_hand == "scissors" and p2_hand == "paper")
        ):
            # user wins, give 6 points
            points += 6

        points += {"rock": 1, "paper": 2, "scissors": 3}[p1_hand]

    print(points)


def translate_input(inp: str):
    translate = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    translation = inp.maketrans(translate)
    return inp.translate(translation)


if __name__ == "__main__":
    main()
