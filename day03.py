import collections
import re



def p1(fp):

    lines = []

    
    with open(fp) as f:
        for line in f:
            line = line.strip()
            lines.append(line)
    
    total = 0
    for i,line in enumerate(lines):
        vv = re.finditer(r'(\d+)', line)
        for match in vv:
            # check
            i1, i2 = match.span()
            v = int(line[i1:i2])
            # left
            if i1>0 and line[i1-1] != '.':
                total += v
                continue
            # right
            if i2<len(line) and line[i2] != '.':
                total += v
                continue
            # up
            if i>0:
                i1up = max(i1-1, 0)
                i2up = min(i2+1, len(line))
                up = lines[i-1][i1up:i2up]
                if up != ('.'*(i2up-i1up)):
                    total += v
                    continue
            
            #down
            if i<len(lines)-1:
                i1down = max(i1-1, 0)
                i2down = min(i2+1, len(line))
                down = lines[i+1][i1down:i2down]
                if down != ('.'*(i2down-i1down)):
                    total += v
                    # continue
    print(total)



def p2(fp):
    lines = []
    with open(fp) as f:
        for line in f:
            line = line.strip()
            lines.append(line)
    
    num_match = []
    for i,line in enumerate(lines):
        num_match.append(list(re.finditer(r'(\d+)', line)))
        

    gerz = collections.defaultdict(list)
    for i,line in enumerate(lines):
        sym = re.finditer(r'\*', line)
        for sm in sym:
            idx = sm.span()[0]
            
            # left right
            li = max(idx-1, 0)
            ri = min(idx+1, len(line)-1)
            for nm in num_match[i]:
                a,b = nm.span()
                val = int(lines[i][a:b])
                if a==li or a==ri or b-1==li or b-1==ri:
                    gerz[(i, idx)].append(val)
            
            # top
            if i > 0:
                for nm in num_match[i-1]:
                    a,b = nm.span()
                    val = int(lines[i-1][a:b])
                    if (a >= li and a<=ri) or (b-1>=li and b-1<=ri):
                        gerz[(i, idx)].append(val)
            
            if i < len(lines)-1:
                for nm in num_match[i+1]:
                    a,b = nm.span()
                    val = int(lines[i+1][a:b])
                    if (a >= li and a<=ri) or (b-1>=li and b-1<=ri):
                        gerz[(i, idx)].append(val)
    
    ratios = 0
    for _,v in gerz.items():
        if len(v) != 2:
            continue
        ratios += v[0] * v[1]
    print(ratios)



if __name__ == '__main__':
    fp = 'input.txt'
    p1(fp)
    p2(fp)