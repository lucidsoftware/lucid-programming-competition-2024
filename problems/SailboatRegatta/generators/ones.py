import random

random.seed(42)

if __name__ == "__main__":
    W = int(input())
    L = int(input())
    K = int(input())
    print(f"{W} {L} {K}")
    for y in range(L):
        line = ""
        for x in range(W):
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            line += f"{dx},{dy} "
        print(line)
