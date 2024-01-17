import collections
import re
import numpy as np


regex = re.compile(r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)')


def is_subset(s1, s2):
    for v in s1:
        if v not in s2: return False  
    return True


def solution(fp):
    bricks = []
    # x,y,z uvijek >= 0
    xmax, ymax, zmax = -1,-1,-1
    with open(fp) as f:
        for i,line in enumerate(f):
            line = line.strip()
            m = regex.fullmatch(line)
            x1, x2 = int(m.group(1)), int(m.group(4))
            y1, y2 = int(m.group(2)), int(m.group(5))
            z1, z2 = int(m.group(3)), int(m.group(6))
            xmax = max(xmax, x1, x2)
            ymax = max(ymax, y1, y2)
            zmax = max(zmax, z1, z2)
            bricks.append(((x1,x2+1), (y1,y2+1), (z1,z2+1)))
    
    
    grid = np.zeros(shape=(xmax+1, ymax+1, zmax+1), dtype=np.int32)
    for i, ((x1,x2), (y1,y2), (z1,z2)) in enumerate(bricks):
        grid[x1:x2, y1:y2, z1:z2] = i+1
            
            
    # print(grid)
    n = len(bricks)
    zmins = list(map(lambda t:t[2][0],bricks))
    ind_sorted = np.argsort(zmins)
    
    # falldown
    grid_cpy = np.zeros(shape=grid.shape,dtype=np.int32)
    bricks_cpy = [None for _ in range(n)]
    for i in ind_sorted:
        (x1,x2), (y1,y2), (z1,z2) = bricks[i]
        zfall = z1
        for z in range(zfall-1, -1, -1):
            blw = grid_cpy[x1:x2, y1:y2, z]
            if np.any((blw!=0)): break
            zfall = z
        
        
        
        # pomakni sve dolje
        zlen = z2-z1
        zup = zfall+zlen
        bricks_cpy[i] = ((x1,x2), (y1,y2), (zfall, zup))
        grid_cpy[x1:x2, y1:y2, zfall:zup] = i+1
    
    
    
    supports = list(map(lambda _:set(), range(n)))
    for i,t in enumerate(bricks_cpy):
        (x1,x2), (y1,y2), (_,z2) = t
        above = grid_cpy[x1:x2, y1:y2, z2]
        unq = np.unique(above)
        unq = unq[unq!=0] - 1
        supports[i].update(unq)
        
    
    supportedby = list(map(lambda _:set(), range(n)))
    for i,s in enumerate(supports):
        for j in s: supportedby[j].add(i)
    
    
    def supall(i):
        sa = set()
        q = collections.deque()
        q.append(i)
        
        while len(q)>0:
            x = q.popleft()
            vs = supports[x]
            for v in vs:
                if v not in sa:
                    q.append(v)
                    sa.add(v)
        
        return sa
    
    supports_all = list(map(supall, range(n))) 
        
        
    
    def safe__(i):
        sup = supports[i]
        for s in sup:
            qq = supportedby[s]
            if len(qq)<2: return False
        return True
    safe = list(map(safe__, range(n)))
    print(sum(safe))
    
    
    def othrz(i):
        if safe[i]: return 0
        
        saa = supports_all[i]
        falling = set(); falling.add(i)
        recheck = collections.deque(saa)
        
        while len(recheck)>0:
            x = recheck.popleft()
            if x in falling: continue
            
            sby = supportedby[x]
            # x će padati ako padaju svi koji ga drže
            fall = True
            for v in sby:
                if v!=i and v not in saa:
                    fall = False
                    break 
                if v not in falling:
                    fall = False
                    break
                
            if fall:
                falling.add(x)
                recheck.extend(supports[x])
        
        return len(falling)-1
        
    
    print(sum(map(othrz, range(n))))
                


if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)