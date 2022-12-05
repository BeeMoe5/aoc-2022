def main():
    with open("input.txt", "r") as file:
        inputs = file.read().split("\n\n")
        inputs = map(lambda food: sum([int(f) for f in food.splitlines()]), inputs)

    largest = None
    for inp in inputs:
        if largest:
            largest = inp if inp > largest else largest
        else:
            largest = inp

    print(largest)


if __name__ == "__main__":
    main()
