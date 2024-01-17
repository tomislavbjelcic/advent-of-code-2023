import itertools


def solution(fp):
    
    raw = list(map(str.strip, open(fp)))

    rock_coords = []
    for i,row in enumerate(raw):
        for j in range(len(row)):
            if row[j] == '#':
                rock_coords.append((i,j))

    factor_p1, distances_p1 = 2, 0
    factor_p2, distances_p2 = 1000000, 0
    eridx, ecidx = find_empty(raw)
    for (i1,j1),(i2,j2) in itertools.combinations(rock_coords, 2):
        x_num_between = 0
        for eri in eridx:
            if eri>min(i1,i2) and eri<max(i1,i2):
                x_num_between += 1
        
        y_num_between = 0
        for eci in ecidx:
            if eci>min(j1,j2) and eci<max(j1,j2):
                y_num_between += 1

        xdiff1 = abs(i1-i2)+(factor_p1-1)*x_num_between
        ydiff1 = abs(j1-j2)+(factor_p1-1)*y_num_between
        distances_p1 += xdiff1+ydiff1
        
        xdiff2 = abs(i1-i2)+(factor_p2-1)*x_num_between
        ydiff2 = abs(j1-j2)+(factor_p2-1)*y_num_between
        distances_p2 += xdiff2 + ydiff2
    
    print(distances_p1)
    print(distances_p2)

        



def find_empty(raw):
    num_cols = len(raw[0])
    num_rows = len(raw)
    # find empty rows
    empty_rows_idx = set()
    for i,row in enumerate(raw):
        if '#' not in row:
            empty_rows_idx.add(i)
    
    # find empty cols
    empty_cols_idx = set()
    for j in range(num_cols):
        has_g = False
        for i in range(num_rows):
            if raw[i][j] == '#':
                has_g = True
                break
        
        if not has_g:
            empty_cols_idx.add(j)

    return empty_rows_idx,empty_cols_idx


if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)