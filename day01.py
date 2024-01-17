import re


def p1(fp):
    pat = re.compile(r'\d')
    total = 0
    for line in open(fp):
        digits = pat.findall(line)
        total += int(digits[0] + digits[-1])
    print(total)
        

def p2(fp):
    words = ['one', 'two', 'three', 
             'four', 'five', 'six', 
             'seven', 'eight', 'nine']
    wd = dict(map(lambda i:(str(i),i),range(1,10)))
    for i,w in enumerate(words, start=1): wd[w] = i
    total = 0
    pat = re.compile(
        f"(?=({'|'.join(wd.keys())}))"
    )
    for line in open(fp):
        digits = pat.findall(line)
        total += wd[digits[0]] * 10 + wd[digits[-1]]
    print(total)


if __name__ == '__main__':
    fp = 'input.txt'
    p1(fp)
    p2(fp)