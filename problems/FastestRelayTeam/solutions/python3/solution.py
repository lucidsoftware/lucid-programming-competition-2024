def get_fastest_time(swimmers):
    # Try every combination
    fastest_time = 4001 # Worst time possible is 1000*4
    num_swimmers = len(swimmers)
    for i in range(num_swimmers):
        for j in range(num_swimmers):
            if j != i:
                for k in range(num_swimmers):
                    if k != i and k != j:
                        for l in range(num_swimmers):
                            if l != i and l != j and l != k:
                                time = swimmers[i][0] + swimmers[j][1] + swimmers[k][2] + swimmers[l][3]
                                fastest_time = min(time, fastest_time)
    return fastest_time

def insert_swimmer(swimmer, fastest_for_stroke):
    # Insert swimmer into stroke
    for i in range(min(4, len(fastest_for_stroke))):
        if swimmer[1] <= fastest_for_stroke[i][1]:
            fastest_for_stroke.insert(i, swimmer)
            return
        elif i == 3:
            return
    fastest_for_stroke.append(swimmer)

def populate_fastest_for_stroke(swimmers, stroke) -> list[tuple[int, int]]:
    # prepopulate with first 4 swimmers
    fastest_for_stroke = []
    for i in range(len(swimmers)):
        insert_swimmer((i, swimmers[i][stroke]), fastest_for_stroke)
    return fastest_for_stroke

if __name__=="__main__":
    # Parse input - O(n)
    num_swimmers = int(input())
    swimmers = []
    for _ in range(num_swimmers):
        swimmer = list(int(x) for x in input().split())
        swimmers.append(swimmer)

    # Condense down to 16 fastest swimmers - O(n)
    fastest_for_strokes = [[]]
    fastest_swimmers_list = []
    for i in range(4):
        fastest_for_strokes.append(populate_fastest_for_stroke(swimmers, i)[:4])
        fastest_swimmers_list.extend(x[0] for x in fastest_for_strokes[i])
    # Remove duplicates
    fastest_swimmers_indexes = set(fastest_swimmers_list)
    fastest_swimmers = []
    for i in range(len(swimmers)):
        if i in fastest_swimmers_indexes:
            fastest_swimmers.append(swimmers[i])    
    
    # Try every combination - O(4^4) - O(1)
    print(get_fastest_time(fastest_swimmers))
