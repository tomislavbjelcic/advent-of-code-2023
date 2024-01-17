import re
import math



def travel(dd, start, end_set, instructions):
    el = start
    mod = len(instructions)
    step = 0
    
    while True:
        idx = int(instructions[step%mod]=='R')
        el = dd[el][idx]
        step += 1
        if el in end_set: return step

    
def solution(fp):
    instructions = None
    dd = None
    with open(fp) as f:
        instructions = f.readline().strip()
        f.readline()
        dd = {}
        for line in f:
            line = line.strip()
            source, left, right = re.findall(r'\w\w\w', line)
            dd[source] = (left, right)
    
    print(travel(dd, 'AAA', ['ZZZ'], instructions))
    starting = []
    ending = []
    for k in dd.keys():
        if k[-1] == 'A': starting.append(k)
        if k[-1] == 'Z': ending.append(k)
    ending = set(ending)
    
    # namjesten input...
    step_list = list(map(lambda st: travel(dd, st, ending, instructions), starting))
    print(math.lcm(*step_list))
    


if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)