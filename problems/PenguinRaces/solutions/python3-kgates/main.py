class Penguin:
    def __init__(self, name: str, time: int):
        self.name = name
        self.time = time

    def __gt__(self, other):
        return self.time > other.time


def main():
    num_penguins = int(input())
    penguins = []
    for i in range(num_penguins):
        raw_penguin = input()
        penguin = raw_penguin.split(' - ')
        penguins.append(Penguin(penguin[0], int(penguin[1])))
    penguins.sort()
    print("First: " + penguins[0].name)
    print("Second: " + penguins[1].name)
    print("Third: " + penguins[2].name)


main()
