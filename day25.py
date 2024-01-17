import collections
import networkx as nx




def solution(fp):
    g = collections.defaultdict(set)
    with open(fp) as f:
        for line in f:
            line = line.strip()
            k = line[:3]
            rest = line[5:].split()
            for r in rest:
                g[k].add(r)
                g[r].add(k)
    
    gx = nx.Graph()
    gx.add_nodes_from(g.keys())
    for k,vs in g.items():
        for v in vs:
            gx.add_edge(k, v)
    
    
    cs = nx.minimum_edge_cut(gx)
    for x,y in cs:
        gx.remove_edge(x,y)
        
    aa = list(map(len, nx.connected_components(gx)))
    print(aa[0]*aa[1])
    



if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)