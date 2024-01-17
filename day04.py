import re
import collections


def p1(fp):
    
    pat = re.compile(r'''
        Card\s+(?P<card_id>\d+):\s*
        (?P<numbers>(\d+\s*)*\d+)
        \s*\|\s*
        (?P<winning>(\d+\s*)*\d+)
        \s*
        ''', re.VERBOSE)
    
    points = 0
    with open(fp) as f:
        for line in f:
            mat = pat.match(line)
            numbers = list(map(int, mat.group('numbers').split()))
            winning = set(map(int, mat.group('winning').split()))
            hits = len(winning.intersection(numbers))
            points += (1 << hits-1) if hits>0 else 0
    print(points)
            
        



def p2(fp):
    
    pat = re.compile(r'''
        Card\s+(?P<card_id>\d+):\s*
        (?P<numbers>(\d+\s*)*\d+)
        \s*\|\s*
        (?P<winning>(\d+\s*)*\d+)
        \s*
        ''', re.VERBOSE)
    
    cards = collections.defaultdict(lambda: 1)
    with open(fp) as f:
        for line in f:
            mat = pat.match(line)
            card_id = int(mat.group('card_id'))
            card_count = cards[card_id]
            numbers = list(map(int, mat.group('numbers').split()))
            winning = set(map(int, mat.group('winning').split()))
            hits = len(winning.intersection(numbers))
            for i in range(card_id+1, card_id+1+hits):
                cards[i] += card_count
            
    print(sum(cards.values()))



if __name__ == '__main__':
    fp = 'input.txt'
    p1(fp)
    p2(fp)