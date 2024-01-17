import numpy as np


def solution(fp):
    
    total_p1, total_p2 = 0, 0
    with open(fp) as f:

        block = []
        for line in f:
            line = line.strip()
            if len(line)==0:
                block_np = np.array(block,dtype=np.int8)
                total_p1 += summarize(block_np, d=0)
                total_p2 += summarize(block_np, d=1)
                block.clear()
            else:
                rr = list(map(lambda c:int(c=='#'), line))
                block.append(rr)
        
        block_np = np.array(block,dtype=np.int8)
        total_p1 += summarize(block_np, d=0)
        total_p2 += summarize(block_np, d=1)


    print(total_p1)
    print(total_p2)




def find_horizontal(block, d):
    blen = len(block)
    for i in range(blen-1):
        diff = diff_horizontal(block, i)
        ds = np.sum(diff)
        if ds==d:
            return i
        
        
    return -1


def diff_horizontal(block, i):
    aa = block[:i+1]
    bb = block[i+1:]
    aa = aa[::-1]
    xxx = min(len(aa), len(bb))
    aa = aa[:xxx]
    bb = bb[:xxx]
    return np.abs(aa-bb)


def summarize(block: np.array, d):
    fh = find_horizontal(block, d)
    if fh!=-1: return 100*(fh+1)
    return find_horizontal(block.T, d)+1
    

if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)