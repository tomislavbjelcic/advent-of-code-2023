
def index_of(l: list, el):
    return l.index(el) if el in l else -1


def p1(fp):
    print(sum(map(hsh, open(fp).read().strip().split(','))))

def p2(fp):
    
    splitted = open(fp).read().strip().split(',')
    
    boxes = [([], []) for _ in range(256)]
    for spl in splitted:
        if spl[-1]=='-':
            lbl = spl[:-1]
            box_idx = hsh(lbl)
            labels = boxes[box_idx][0]
            idx = index_of(labels, lbl)
            if idx != -1:
                labels.pop(idx)
                boxes[box_idx][1].pop(idx)
        else:
            lbl, fl = spl.split('=')
            fl = int(fl)
            box_idx = hsh(lbl)
            labels, flens = boxes[box_idx]
            idx = index_of(labels, lbl)
            if idx != -1:
                flens[idx] = fl
            else:
                labels.append(lbl)
                flens.append(fl)
    
    
    fpower = 0
    for i,(labels, flens) in enumerate(boxes):
        for slot, (lbl, fl) in enumerate(zip(labels, flens)):
            fpower += (i+1) * (slot+1) * fl
    
    print(fpower)




def hsh(s: str) -> int:
    v = 0
    for c in s: v = ((v+ord(c))*17)%256
    return v


if __name__ == '__main__':
    fp = 'input.txt'
    p1(fp)
    p2(fp)