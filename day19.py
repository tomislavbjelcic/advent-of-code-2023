import math
import re

# px{a<2006:qkq,m>2090:A,rfg}
regex1 = re.compile(r'(\w+)\{(.+,)(\w+)\}')
regex2 = re.compile(r'([xmas])([<>])(\d+):(\w+),')
regex3 = re.compile(r'([xmas])=(\d+)')


def load(fp):
    workflows = {}
    inz = []
    with open(fp) as f:
        for line in f:
            line = line.strip()
            if len(line)==0: break
            m1 = regex1.fullmatch(line)
            name, wf, default = m1.groups()
            workflow_list = []
            for m in regex2.finditer(wf):
                part, eqs, num, to = m.groups()
                num = int(num)
                workflow_list.append((part, eqs=='<', num, to))
            workflows[name] = (workflow_list, default)
                
        
        for line in f:
            line = line.strip()
            part_dict = {}
            for m in regex3.finditer(line): part_dict[m.group(1)] = int(m.group(2))
            inz.append(part_dict)
            
    return workflows, inz
        


def p1(fp):
    workflows, inz = load(fp)
    total = 0
    for part in inz:
        cur = 'in'
        while True:
            wf, df = workflows[cur]
            for k,eqs,cv,nxt in wf:
                v = part[k]
                if v==cv: continue
                if (v<cv)==eqs:
                    df = nxt
                    break

            if df=='R': break
            if df=='A':
                total += sum(part.values())
                break
            cur = df


    print(total)



def p2(fp):
    
    workflows, _ = load(fp)
    rn = (1,4000)
    # (wfn, [x, m, a, s] ranges)
    d = {n:i for i,n in enumerate('xmas')}
    start = ('in', [rn, rn, rn, rn])
    q = [start]

    total = 0
    while len(q)>0:
        st = q.pop()
        wfn, rr = st
        if wfn=='A':
            total += math.prod(map(lambda t:t[1]-t[0]+1, rr))
            continue
        if wfn=='R': continue
        
            
        wf, df = workflows[wfn]
        brk = False
        for k,eqs,cv,nxt in wf:
            ii = d[k]
            v1, v2 = rr[ii]
            if eqs:
                # znak <
                v2new = min(v2, cv-1)
                if v1<=v2new:
                    rrc = rr.copy()
                    rrc[ii] = (v1, v2new)
                    q.append((nxt, rrc))
                v1up = v2new+1
                if v1up<=v2: rr[ii] = (v1up, v2)
                else: brk=True
            
            else:
                # znak >
                v1new = max(v1, cv+1)
                if v1new<=v2:
                    rrc = rr.copy()
                    rrc[ii] = (v1new, v2)
                    q.append((nxt, rrc))
                v2down = v1new-1
                if v1<=v2down: rr[ii] = (v1, v2down)
                else: brk=True
            
            if brk: break

        if not brk: q.append((df, rr))
            
                   
    print(total)
            
            

if __name__ == '__main__':
    fp = 'input.txt'
    p1(fp)
    p2(fp)