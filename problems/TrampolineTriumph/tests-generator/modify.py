if __name__=="__main__":
    players_count = int(input())
    factors = list(map(float, input().split()))
    milestones_count = int(input())
    milestones = [list(map(float, input().split())) for _ in range(milestones_count)]
    print(players_count)
    print(' '.join(["{:.6f}".format(factor) for factor in factors]))
    print(milestones_count)
    for milestone in milestones:
        print(' '.join(["{:.6f}".format(value) for value in milestone[:-1]]))
