def main():
    with open("input.txt", "r") as file:
        inputs = file.read().split("\n\n")
        inputs = list(
            map(lambda food: sum([int(f) for f in food.splitlines()]), inputs)
        )
        inputs.sort(reverse=True)
        print(sum((inputs[0], inputs[1], inputs[2])))


if __name__ == "__main__":
    main()
