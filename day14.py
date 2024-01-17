import numpy as np


def cube_rocks(mat):
    n_rows, n_cols = mat.shape
    cr_rows = []
    for i in range(n_rows):
        crr = [-1]
        for j in range(n_cols):
            if mat[i,j] == '#':
                crr.append(j)
        crr.append(n_cols)
        cr_rows.append(crr)

    cr_cols = []
    for j in range(n_cols):
        crc = [-1]
        for i in range(n_rows):
            if mat[i,j] == '#':
                crc.append(i)
        crc.append(n_rows)
        cr_cols.append(crc)
    return cr_rows, cr_cols

def north_south(mat: np.ndarray, cr_cols, north):
    for j,a in enumerate(cr_cols):
        for i in range(len(a)-1):
            fi = a[i]
            si = a[i+1]
            if si-fi<2: continue
            substr = mat[fi+1:si, j]
            count = np.sum(substr=='O')
            if count==0: continue
            substr[:count] = 'O'
            substr[count:] = '.'
            mat[fi+1:si, j] = substr if north else substr[::-1]


def west_east(mat: np.ndarray, cr_rows, west):
    for i,a in enumerate(cr_rows):
        for j in range(len(a)-1):
            fi = a[j]
            si = a[j+1]
            if si-fi<2: continue
            substr = mat[i, fi+1:si]
            count = np.sum(substr=='O')
            if count==0: continue
            substr[:count] = 'O'
            substr[count:] = '.'
            mat[i, fi+1:si] = substr if west else substr[::-1]



def load(mat):
    tot = 0
    n_rows, n_cols = mat.shape
    for i in range(n_rows):
        for j in range(n_cols):
            if mat[i,j] == 'O':
                tot += n_rows - i
    return tot


def ha(mat):
    return hash(''.join(map(lambda r: ''.join(r), mat)))



def p1(fp):
    mat = []
    with open(fp) as f:
        for line in f:
            r = list(line.strip())
            mat.append(r)

    mat = np.array(mat)
    _, cr_cols = cube_rocks(mat)
    
    north_south(mat, cr_cols, north=True)
    print(load(mat))


def p2(fp):
    mat = []
    with open(fp) as f:
        for line in f:
            r = list(line.strip())
            mat.append(r)

    mat = np.array(mat)
    cr_rows, cr_cols = cube_rocks(mat)

    n_cycles = 1000000000
    loads = [load(mat)]
    hashes = {ha(mat):0}

    for i in range(1,n_cycles+1):
        north_south(mat, cr_cols, north=True)
        west_east(mat, cr_rows, west=True)
        north_south(mat, cr_cols, north=False)
        west_east(mat, cr_rows, west=False)

        h = ha(mat)
        if h in hashes:
            idx = hashes[h]
            cycle_len = i - idx
            v = (n_cycles - idx)%cycle_len
            v = idx + v
            print(loads[v])
            return
        
        hashes[h] = i
        loads.append(load(mat))




if __name__ == '__main__':
    fp = 'input.txt'
    p1(fp)
    p2(fp)