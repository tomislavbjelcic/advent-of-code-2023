import itertools
from bitarray.util import zeros


pdict = {(1,0):'v', (-1,0):'^', (0,1):'>', (0,-1):'<'}


def within(r, c, nr, nc):
    return 0<=r<nr and 0<=c<nc


def neigh(r, c, nr, nc, grid, v):
    tr,tc = r+1, c
    if within(tr, tc, nr, nc) and grid[tr][tc]!='#': v.append((tr,tc))
    tr,tc = r-1, c
    if within(tr, tc, nr, nc) and grid[tr][tc]!='#': v.append((tr,tc))
    tr,tc = r, c+1
    if within(tr, tc, nr, nc) and grid[tr][tc]!='#': v.append((tr,tc))
    tr,tc = r, c-1
    if within(tr, tc, nr, nc) and grid[tr][tc]!='#': v.append((tr,tc))


def find_next(r, c, rprev, cprev, grid, nr, nc, intersections_inv, slopes_flag):
    plen = 1
    neighbors = []
    while (r,c) not in intersections_inv:
        if slopes_flag and grid[r][c] != '.' and pdict[(r-rprev,c-cprev)] != grid[r][c]:
            return None
        plen += 1
        neighbors.clear(); neigh(r, c, nr, nc, grid, neighbors)
        # len(neighbors) mora nužno biti 2
        # assert len(neighbors)==2
        for r_, c_ in neighbors:
            if r_!=rprev or c_!=cprev:
                rprev, cprev = r, c
                r, c = r_, c_
                break
    return r,c,plen
                
                
                

def dfs(start, goal, g):
    
    ba = zeros(len(g))
    ba[start] = 1
    q = [(0, ba, start)]
    res = []
    
    while len(q)>0:
        dist, ba, n = q.pop()
        if n==goal:
            res.append(dist)
            continue
        
        for m,d in g[n]:
            if ba[m]==1: continue
            bacpy = ba.copy()
            bacpy[m] = 1
            q.append((dist+d, bacpy, m))
            
    return res
    



def longest_hike(grid, slopes_flag):
    nr = len(grid)
    nc = len(grid[0])
    intersections = []
    v = []
    for i,j in itertools.product(range(nr), range(nc)):
        if grid[i][j] == '#': continue
        v.clear(); neigh(i,j,nr,nc,grid,v)
        if len(v)==1 or len(v)>=3: intersections.append((i,j))
    intersections_inv = {t:i for i,t in enumerate(intersections)}
            
            
    # pronađi koja raskrižja su povezana
    n = len(intersections)
    g = [[] for _ in range(n)]
    for i, (rint, cint) in enumerate(intersections):
        v.clear(); neigh(rint, cint, nr, nc, grid, v)
        for r_, c_ in v:
            fnext = find_next(r_, c_, rint, cint, grid, nr, nc, intersections_inv, slopes_flag)
            if fnext is None: continue
            rnext, cnext, plen = fnext
            g[i].append((intersections_inv[(rnext, cnext)],plen))
    
    sr, sc = 0, 1
    er, ec = nr-1, nc-2
    start = intersections_inv[(sr,sc)]
    goal = intersections_inv[(er,ec)]
    return max(dfs(start, goal, g))



def solution(fp):
    grid = list(map(str.strip, open(fp)))
    print(longest_hike(grid, True))
    print(longest_hike(grid, False))


if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)