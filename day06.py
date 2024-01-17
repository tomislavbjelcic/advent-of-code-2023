from math import sqrt, floor, ceil


def num_ways(t, d):
    # f(h) = h^2 - ht + d < 0
    # h12 = t +- sqrt(t^2 - 4d) / 2
    discr = t*t - 4*d
    if discr<0:
        return t+1
    h1 = (t-sqrt(discr))/2
    h2 = d/h1
    if h1<0:
        return floor(h2)
    if h2<1:
        return 0
    return floor(h2) - ceil(h1) + 1


def p1(fp):
    times = None
    distances = None
    with open(fp) as f:
        
        times = list(map(int,f.readline().split(':')[1].split()))
        distances = list(map(int,f.readline().split(':')[1].split()))

    tot = 1
    for t,d in zip(times, distances):
        tot *= num_ways(t,d)

    print(tot)
    
    
    
def p2(fp):
    time = None
    distance = None
    with open(fp) as f:
        
        time = int(''.join(f.readline().split(':')[1].split()))
        distance = int(''.join(f.readline().split(':')[1].split()))
    
    print(num_ways(time, distance))



if __name__ == '__main__':
    fp = 'input.txt'
    p1(fp)
    p2(fp)