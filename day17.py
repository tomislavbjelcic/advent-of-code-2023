from astar import AStar



def within(r, c, nr, nc):
    return (0<=r<nr) and (0<=c<nc)


def manhattan(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)



def expand(st, nr, nc, rem_cond_turn, rem_cond_straight):
    if st is None:
        return [(0, 0, 0, 1, 1), (0, 0, 1, 0, 1)]
    
    r, c, dr, dc, rem = st
    exp = []
    rf, cf = r+dr, c+dc
    if within(rf, cf, nr, nc) and rem_cond_straight(rem+1):
        exp.append((rf, cf, dr, dc, rem+1))
        
    if not rem_cond_turn(rem): return exp
    
    if dr==0:
        rl, cl, drl, dcl = r-1, c, -1, 0
        rr, cr, drr, dcr = r+1, c, 1, 0
    else:
        rl, cl, drl, dcl = r, c-1, 0, -1
        rr, cr, drr, dcr = r, c+1, 0, 1

    if within(rl, cl, nr, nc):
        exp.append((rl, cl, drl, dcl, 1))
    
    if within(rr, cr, nr, nc):
        exp.append((rr, cr, drr, dcr, 1))
    
    return exp



def minimize_heat_loss(heat_loss, end, ef):
    
    alg = MojAStar(heat_loss, ef)
    path = list(alg.astar(None, end))
    hl = 0
    for i in range(2, len(path)):
        r,c,_,_,_ = path[i]
        hl += heat_loss[r][c]
    return hl



class MojAStar(AStar):
    def __init__(self, heat_loss, ef):
        self.heat_loss = heat_loss
        self.ef = ef

    def neighbors(self, node):
        return self.ef(node)
    

    def distance_between(self, n1, n2):
        rn2, cn2, _, _, _ = n2
        return self.heat_loss[rn2][cn2]
            
    def heuristic_cost_estimate(self, current, goal):
        if current is None: return 0
        r1, c1, _, _, _ = current
        r2, c2, _, _, _ = goal
        return manhattan(r1, c1, r2, c2)
    
    
    def is_goal_reached(self, current, goal):
        if current is None: return False
        return current[0]==goal[0] and current[1]==goal[1]
    
    

def solution(fp):
    heat_loss = []
    with open(fp) as f:
        for line in f:
            line = line.strip()
            heat_loss.append(list(map(int, line)))
            
    nr = len(heat_loss)
    nc = len(heat_loss[0])
    end = (nr-1, nc-1, 0, 0, 0)
       
    rem_cond_turn_p1 = lambda _:True
    rem_cond_straight_p1 = lambda rem:rem<=3
    ef_p1 = lambda st: expand(st, nr, nc, rem_cond_turn_p1, rem_cond_straight_p1)
    print(minimize_heat_loss(heat_loss, end, ef_p1))
    
    rem_cond_turn_p2 = lambda rem:rem>=4
    rem_cond_straight_p2 = lambda rem:rem<=10
    ef_p2 = lambda st: expand(st, nr, nc, rem_cond_turn_p2, rem_cond_straight_p2)
    print(minimize_heat_loss(heat_loss, end, ef_p2))


    
    

if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)
    