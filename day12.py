import functools

def solution(fp):
    
    total_p1, total_p2 = 0, 0
    with open(fp) as f:
        for line in f:
            
            line = line.strip()
            s, pos = line.split()
            pos = tuple(map(int, pos.split(',')))
            total_p1 += arrangements(s.strip('.'), pos)
            
            s = '?'.join([s]*5)
            pos = pos*5
            total_p2 += arrangements(s.strip('.'), pos)
    
    print(total_p1)
    print(total_p2)
            

@functools.cache
def arrangements(s: str, pos: tuple) -> int:
    
    if len(pos)==0: return int('#' not in s)
    
    singl = len(pos)==1
    pp = pos[0]
    spaces = len(s) - (sum(pos) - pp) - (len(pos)-1)
    shifts = spaces - pp + 1
    if shifts<=0: return 0
    
    total = 0
    for sh in range(shifts):
        if '#' in s[:sh]: break
        if '.' in s[sh:sh+pp]: continue
        if not singl and s[sh+pp] == '#': continue
        
        nextidx = (sh + pp) + int(not singl)
        total += arrangements(s[nextidx:].strip('.'), pos[1:])
        
    return total



if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)
    
    
    
    
    

    