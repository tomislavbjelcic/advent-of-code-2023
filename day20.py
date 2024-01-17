import collections
import math


def revg(graph):
    gr = {}
    for k,vl in graph.items():
        for v in vl:
            if v not in gr: gr[v] = []
            gr[v].append(k)
    return gr



def push_button(graph, bcast, state, flip_flops, outs, last_conj, bp, kancer):
    hps, lps = 0, 1
    q = collections.deque()
    # (from, to, pulse) #from je None ako je broadcaster
    for bc in bcast: q.append((None, bc, False))

    while len(q)>0:
        frm, tom, p = q.popleft()
        
        if p: hps += 1
        else: lps += 1
        if tom in outs: continue
        
        
        if tom in flip_flops:
            if p: continue
            on = state[tom]
            state[tom] = not on
            send = not on
            for nn in graph[tom]: q.append((tom, nn, send))
                
        else:
            inz = state[tom]
            inz[frm] = p
            send = not p or not all(inz.values())
            for nn in graph[tom]: q.append((tom, nn, send))
            
            if tom==last_conj and p:
                kancer[frm].append(bp)
    
    return hps, lps
                    


def solution(fp):
    graph = {}
    bcast = None
    flip_flops = set()
    with open(fp) as f:
        for line in f:
            line = line.strip()
            spl = line.split(' -> ')
            module, neigh = spl
            neigh = neigh.strip().split(', ')
            if module=='broadcaster':
                bcast = neigh
                continue

            module = module.strip()
            typ = module[0]
            module = module[1:]
            graph[module] = neigh
            if typ=='%': flip_flops.add(module)
    
    keyz = graph.keys()
    outs = set()
    for vl in graph.values():
        for v in vl:
            if v not in keyz:
                outs.add(v)

    
    gr = revg(graph)
    state = {}
    # name -> on(T/F) (ako je %) ili dict zapamćenih ulaza (ako je &)
    for k in graph:
        if k in flip_flops: state[k] = False
        else:
            inz = gr[k]
            d = dict(map(lambda mn:(mn,False), inz))
            state[k] = d
    
    
    out = list(outs)[0]
    last_conj = gr[out][0]
    kancer = dict(map(lambda kk:(kk,[]), gr[last_conj]))
    hp, lp = 0, 0
    for bp in range(20000):
        x, y = push_button(graph, bcast, state, 
                           flip_flops, outs, last_conj, 
                           bp, kancer)
        if bp<1000: hp += x; lp += y
    
    ggez = []
    for vl in kancer.values():
        ggez.append(vl[-1] - vl[-2])
    
    print(hp * lp)
    print(math.lcm(*ggez))
        


if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)