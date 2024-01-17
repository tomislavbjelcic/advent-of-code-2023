from collections import Counter
from functools import cmp_to_key

    
strengths_p1 = {'T': 10, 'J':11, 'Q':12, 'K':13, 'A':14}
for i in range(2,10): strengths_p1[str(i)] = i

strengths_p2 = {'T': 10, 'J':1, 'Q':12, 'K':13, 'A':14}
for i in range(2,10): strengths_p2[str(i)] = i


def hand_score(counter: Counter) -> int:
    n_diff = len(counter)
    if n_diff == 5: return 0
    if n_diff == 1: return 100
    if n_diff == 4: return 1
    _, mc = counter.most_common(1)[0]
    if n_diff == 3: return 3 if mc==3 else 2
    if n_diff == 2: return 70 if mc==4 else 50
    
    
def cmp(a, b, strengths):
    h1, hc1, _ = a
    h2, hc2, _ = b
    hs_diff = hand_score(hc1) - hand_score(hc2)
    if hs_diff != 0: return hs_diff
    
    for x,y in zip(h1, h2):
        d = strengths[x] - strengths[y]
        if d != 0: return d
        
    return 0
        


def p1(fp):
    hands = []
    with open(fp) as f:
        for line in f:
            hand, bid = line.strip().split()
            bid = int(bid)
            hand_counter = Counter(hand)
            hands.append((hand, hand_counter, bid))
    
    compare = lambda a,b: cmp(a,b,strengths_p1)    
    hands.sort(key=cmp_to_key(compare))
    winnings = 0
    for i,(_,_,bid) in enumerate(hands, start=1):
        winnings += i * bid
    print(winnings)
    
    
def p2(fp):
    hands = []
    with open(fp) as f:
        for line in f:
            hand, bid = line.strip().split()
            bid = int(bid)
            hand_counter = Counter(hand)
            if 'J' in hand_counter:
                if len(hand_counter) == 1:
                    hand_counter['A'] = 5
                else:
                    mcl = hand_counter.most_common(2)
                    to = mcl[0][0] if mcl[0][0] != 'J' else mcl[1][0]
                    hand_counter[to] += hand_counter['J']
                del hand_counter['J']
            hands.append((hand, hand_counter, bid))
    
    compare = lambda a,b: cmp(a,b,strengths_p2)    
    hands.sort(key=cmp_to_key(compare))
    winnings = 0
    for i,(_,_,bid) in enumerate(hands, start=1):
        winnings += i * bid
    print(winnings)
        
            
        
    
            




if __name__ == '__main__':
    fp = 'input.txt'
    p1(fp)
    p2(fp)