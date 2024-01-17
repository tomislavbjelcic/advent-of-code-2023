import collections


def within(r, c, nr, nc):
    return (0<=r<nr) and (0<=c<nc)



def num_energized(grid, r, c, dr, dc):
    nr = len(grid)
    nc = len(grid[0])
    q = collections.deque()
    # (r, c, dr, dc)
    q.append((r, c, dr, dc))

    # (r, c)
    visited = set()
    states = set()

    while len(q)>0:
        st = q.popleft()
        r, c, dr, dc = st
        if not within(r, c, nr, nc): continue
        if st in states: continue
        
        states.add(st)
        visited.add((r, c))

        ch = grid[r][c]
        
        if ch=='.': q.append((r+dr, c+dc, dr, dc))

        elif ch=='\\':
            if dc==0: q.append((r, c+dr, 0, dr))
            else: q.append((r+dc, c, dc, 0))

        elif ch=='/':
            if dc==0: q.append((r, c-dr, 0, -dr))
            else: q.append((r-dc, c, -dc, 0))


        elif ch=='|':
            if dc==0: q.append((r+dr, c+dc, dr, dc))
            else:
                q.append((r+1, c, 1, 0))
                q.append((r-1, c, -1, 0))

        elif ch=='-':
            if dr==0: q.append((r+dr, c+dc, dr, dc))
            else:
                q.append((r, c+1, 0, 1))
                q.append((r, c-1, 0, -1))

    
    return len(visited)




def solution(fp):

    grid = list(map(str.strip, open(fp)))

    print(num_energized(grid, 0,0,0,1))
    nr = len(grid)
    nc = len(grid[0])

    ne_max = -1
    for r in range(nr):
        ne_max = max(ne_max, num_energized(grid, r, 0, 0, 1))
        ne_max = max(ne_max, num_energized(grid, r, nc-1, 0, -1))

    for c in range(nc):
        ne_max = max(ne_max, num_energized(grid, 0, c, 1, 0))
        ne_max = max(ne_max, num_energized(grid, nr-1, c, -1, 0))

    print(ne_max)

    

if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)