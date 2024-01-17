

def travel(data, x, y, cfx, cfy):
    ch = data[x][y]

    if ch=='S': return x,y
    
    if ch=='.': return None
    
    if ch=='-':
        if cfx==0: return x,y-cfy
        else: return None
    
    if ch=='|':
        if cfy==0: return x-cfx, y
        else: return None
    
    if ch=='L':
        if cfx==-1: return x,y+1
        if cfy==1: return x-1, y
        else: return None
        
    if ch=='J':
        if cfx==-1: return x,y-1
        if cfy==-1: return x-1,y
        else: return None
        
    if ch=='7':
        if cfx==1: return x,y-1
        if cfy==-1: return x+1, y
        else: return None


    if ch=='F':
        if cfx==1: return x,y+1
        if cfy==1: return x+1,y
        else: return None
        
    


def within(x, y, r, c):
    return x>=0 and x<r and y>=0 and y<c


def manhattan(x1, x2, y1, y2):
    return abs(x1-x2) + abs(y1-y2)


def find_loops(data, sx, sy, r, c):
    directions = []
    if sx>0: directions.append((sx-1, sy, 1, 0))
    if sy>0: directions.append((sx, sy-1, 0, 1))
    if sx<r-1: directions.append((sx+1, sy, -1, 0))
    if sy<c-1: directions.append((sx, sy+1, 0, -1))

    loops = []
    for x,y,cfx,cfy in directions:

        loop = []

        while True:
            ret = travel(data, x, y, cfx, cfy)
            if ret is None: break

            nx, ny = ret
            if not within(nx, ny, r, c): break

            loop.append((x,y))

            if nx==x and ny==y:
                # S
                loops.append(loop)
                break
            
            
            x, y, cfx, cfy = nx, ny, x-nx, y-ny
    
    return loops




    
def solution(fp):

    data = list(map(str.strip, open(fp)))
    sx, sy = None, None
    for i,line in enumerate(data):
        for j,ch in enumerate(line):
            if ch=='S':
                sx, sy = i, j
                break
    
    r = len(data)
    c = len(data[0])
    loops = find_loops(data, sx, sy, r, c)
    loop = loops[0]
    print(len(loop)//2)
    
    # Shoelace formula
    num_corners = len(loop)
    area = 0
    for i,(xi,_) in enumerate(loop):
        yn = loop[(i+1)%num_corners][1]
        yp = loop[i-1][1]
        area += xi * (yn - yp)
    area = abs(area)//2
    
    
    # Pickov teorem
    num_interior = area - num_corners//2 + 1
    print(num_interior)




if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)