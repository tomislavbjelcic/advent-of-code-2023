import re
import itertools



# 20, 19, 15 @  1, -5, -3
regex = re.compile(r'([- ]?\d+), ([- ]?\d+), ([- ]?\d+) @ ([- ]?\d+), ([- ]?\d+), ([- ]?\d+)')



def within(x,y,a,b):
    return a<=x<=b and a<=y<=b


def intersects_inside(px1, py1, px2, py2, vx1, vy1, vx2, vy2, a, b):
    det = -vx1*vy2 + vy1*vx2
    rhsx = px2 - px1
    rhsy = py2 - py1
    if det!=0:
        num_cramer_t = -vy2 * rhsx + vx2 * rhsy
        num_cramer_u = vx1 * rhsy - vy1 * rhsx
        if not (num_cramer_t*det >= 0 and num_cramer_u*det >= 0):
            return False
        
        
        middlex = px1*det + num_cramer_t * vx1
        middley = py1*det + num_cramer_t * vy1
        ad = a*det
        bd = b*det
        if det>0: return ad<=middlex<=bd and ad<=middley<=bd
        else: return bd<=middlex<=ad and bd<=middley<=ad
    
      
    kronecker_capelli = vx1 * rhsy - vy2 * rhsx
    if kronecker_capelli != 0:
        # po kronecker-capellijevom teoremu ne sjeku se nikada
        return False
    
    
    # kreću se po istim pravcima
    # ... lmao u mom inputu to se nikad ne dogodi tako da
    return False
    
    


def cpi(a, b):
    _,ay,az = a
    _,by,bz = b
    return ay*bz - by*az



def cpj(a, b):
    ax,_,az = a
    bx,_,bz = b
    return -(ax*bz - bx*az)


def cpk(a, b):
    ax,ay,_ = a
    bx,by,_ = b
    return ax*by - bx*ay


def mat_copy(a):
    n = len(a)
    acpy = [None for _ in range(n)]
    for i in range(n): acpy[i] = a[i].copy()
    return acpy

def insert_col(a, rhs, c):
    n = len(a)
    for i in range(n):
        a[i][c] = rhs[i]
        

def det(M):
    # Bareiss algorithm, copy pasted from
    # https://stackoverflow.com/questions/66192894/precise-determinant-of-integer-nxn-matrix
    
    M = [row[:] for row in M] # make a copy to keep original M unmodified
    N, sign, prev = len(M), 1, 1
    for i in range(N-1):
        if M[i][i] == 0: # swap with another row having nonzero i's elem
            swapto = next( (j for j in range(i+1,N) if M[j][i] != 0), None )
            if swapto is None:
                return 0 # all M[*][i] are zero => zero determinant
            M[i], M[swapto], sign = M[swapto], M[i], -sign
        for j in range(i+1,N):
            for k in range(i+1,N):
                M[j][k] = ( M[j][k] * M[i][i] - M[j][i] * M[i][k] ) // prev
        prev = M[i][i]
    return sign * M[-1][-1]


def solution(fp):
    
    pm, vm = [], []
    
    with open(fp) as f:
        for line in f:
            line = line.strip()
            m = regex.fullmatch(line)
            px, py, pz = int(m.group(1)), int(m.group(2)), int(m.group(3))
            vx, vy, vz = int(m.group(4)), int(m.group(5)), int(m.group(6))
            pm.append((px,py,pz))
            vm.append((vx,vy,vz))
            
    n = len(pm)
    a, b = 200000000000000, 400000000000000
    eh = []
    for i,j in itertools.combinations(range(n), r=2):
        px1, py1, _ = pm[i]
        vx1, vy1, _ = vm[i]
        px2, py2, _ = pm[j]
        vx2, vy2, _ = vm[j]
        if intersects_inside(px1, py1, px2, py2, vx1, vy1, vx2, vy2, a, b):
            eh.append((i,j))
            
    print(len(eh))
    
    v1 = vm[0]
    v2 = vm[1]
    v3 = vm[2]
    p1 = pm[0]
    p2 = pm[1]
    p3 = pm[2]
    
    
    a = [[None for _ in range(6)] for _ in range(6)]
    b = [None for _ in range(6)]
    
    v1x, v1y, v1z = v1
    v2x, v2y, v2z = v2
    v3x, v3y, v3z = v3
    p1x, p1y, p1z = p1
    p2x, p2y, p2z = p2
    p3x, p3y, p3z = p3
    
    a[0][0] = 0
    a[0][1] = p1z - p2z
    a[0][2] = -p1y + p2y
    a[0][3] = 0
    a[0][4] = -v1z + v2z
    a[0][5] = v1y - v2y
    
    a[1][0] = -(p1z - p2z)
    a[1][1] = 0
    a[1][2] = -(-p1x + p2x)
    a[1][3] = -(-v1z + v2z)
    a[1][4] = 0
    a[1][5] = -(v1x - v2x)
    
    a[2][0] = p1y - p2y
    a[2][1] = -p1x + p2x
    a[2][2] = 0
    a[2][3] = -v1y + v2y
    a[2][4] = v1x - v2x
    a[2][5] = 0
     
    a[3][0] = 0
    a[3][1] = p1z - p3z
    a[3][2] = -p1y + p3y
    a[3][3] = 0
    a[3][4] = -v1z + v3z
    a[3][5] = v1y - v3y
    
    a[4][0] = -(p1z - p3z)
    a[4][1] = 0
    a[4][2] = -(-p1x + p3x)
    a[4][3] = -(-v1z + v3z)
    a[4][4] = 0
    a[4][5] = -(v1x - v3x)
    
    a[5][0] = p1y - p3y
    a[5][1] = -p1x + p3x
    a[5][2] = 0
    a[5][3] = -v1y + v3y
    a[5][4] = v1x - v3x
    a[5][5] = 0
    
    # RHS
    b[0] = cpi(v1, p1) - cpi(v2, p2)
    b[1] = cpj(v1, p1) - cpj(v2, p2)
    b[2] = cpk(v1, p1) - cpk(v2, p2)
    b[3] = cpi(v1, p1) - cpi(v3, p3)
    b[4] = cpj(v1, p1) - cpj(v3, p3)
    b[5] = cpk(v1, p1) - cpk(v3, p3)
    
    
    da = det(a)
    a3 = mat_copy(a)
    insert_col(a3, b, 3)
    a4 = mat_copy(a)
    insert_col(a4, b, 4)
    a5 = mat_copy(a)
    insert_col(a5, b, 5)
    x3 = det(a3)//da
    x4 = det(a4)//da
    x5 = det(a5)//da
    print(x3+x4+x5)
    



if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)