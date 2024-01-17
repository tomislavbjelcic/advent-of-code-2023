import collections
import re
import functools
import itertools
                


def within(r, c, nr, nc):
    return 0<=r<nr and 0<=c<nc


def cmap(r, c, nr, nc):
    return r%nr, c%nc



def poly(x, f0, f1, f2):
    d0 = f0
    d1 = f1 - f0
    d2 = ((f2-f1) - d1)//2
    
    return d0 + d1*x + d2*x*(x-1)


def solution(fp):
    grid = list(map(str.strip, open(fp)))

    sr, sc = None, None
    for r,gr in enumerate(grid):
        for c,gc in enumerate(gr):
            if gc=='S':
                sr, sc = r, c

    nr = len(grid)
    nc = len(grid[0])
    visited = set()
    q = collections.deque()
    q.append((sr,sc))
    fi = []
    magic = 26501365
    steps = 64

    for i in itertools.count(1):
        while len(q)>0:
            r, c = q.popleft()

            rne, cne = r+1, c
            mrne, mcne = cmap(rne, cne, nr, nc)
            if grid[mrne][mcne]!='#': visited.add((rne,cne))

            rne, cne = r-1, c
            mrne, mcne = cmap(rne, cne, nr, nc)
            if grid[mrne][mcne]!='#': visited.add((rne,cne))

            rne, cne = r, c+1
            mrne, mcne = cmap(rne, cne, nr, nc)
            if grid[mrne][mcne]!='#': visited.add((rne,cne))

            rne, cne = r, c-1
            mrne, mcne = cmap(rne, cne, nr, nc)
            if grid[mrne][mcne]!='#': visited.add((rne,cne))
            
        
        q.extend(visited)
        visited.clear()
        if i==steps: print(len(q))
        if i%nr == magic%nr:
            fi.append(len(q))
            if len(fi)==3: break



    x = magic//nr
    # print(fi) # [3947, 35153, 97459]
    sol = poly(x, *fi)
    print(sol)



if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)