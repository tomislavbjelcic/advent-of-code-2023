import re
import math



def p1(fp):
    constraints = {'red':12, 'green': 13, 'blue':14}
    pat = re.compile(r'(\d+) (red|green|blue)')
    idsum = 0
    with open(fp) as f:
        for line in f:
            line = line.strip()
            splitted = line.split(':')
            gameid = int(splitted[0].split()[1])
            possible = True
            for num, color in pat.findall(splitted[1]):
                num = int(num)
                if num > constraints[color]:
                    possible = False
                    break
            
            if possible: idsum += gameid
                   
    print(idsum)




def p2(fp):
    powers = []
    with open(fp) as f:
        for line in f:
            line = line.strip()
            splitted = line.split(':')
            splitted = splitted[1].split(';')
            cubemin = {'red':0, 'green':0, 'blue':0}
            for spl in splitted:
                cspl = spl.strip().split(',')
                for cc in cspl:
                    respl = re.findall(r'(\d+) (blue|red|green)', cc)[0]
                    cubemin[respl[1]] = max(int(respl[0]), cubemin[respl[1]])
                    
            powers.append(math.prod(cubemin.values()))

    print(sum(powers))



if __name__ == '__main__':
    fp = 'input.txt'
    p1(fp)
    p2(fp)