import re

regex = re.compile(r'([RLDU]) (\d+) \(#([\dabcdef]{6})\)')
direction_dict = {'R':(1,0), 'L':(-1,0), 'D':(0,1), 'U':(0,-1)}
direction_codes = {0:'R', 1:'D', 2:'L', 3:'U'}


def p1(fp):
    matches = list(regex.finditer(open(fp).read()))
    instructions = []
    for m in matches:
        direction = m.group(1)
        steps = int(m.group(2))
        instructions.append((direction, steps))
    print(lagoon(instructions))
    


def p2(fp):
    matches = list(regex.finditer(open(fp).read()))
    instructions = []
    for m in matches:
        hex_code = m.group(3)
        direction = direction_codes[int(hex_code[-1])]
        steps = int(hex_code[:-1], base=16)
        instructions.append((direction, steps))
    print(lagoon(instructions))
    
    

def lagoon(instructions):
    corners = []
    x, y = 0, 0
    num_points = 0
    for d,s in instructions:
        dx, dy = direction_dict[d]
        x += dx*s
        y += dy*s
        num_points += abs(dx*s) + abs(dy*s)
        corners.append((x, y))
    
    # Shoelace formula
    num_corners = len(corners)
    area = 0
    for i,(xi,_) in enumerate(corners):
        yn = corners[(i+1)%num_corners][1]
        yp = corners[i-1][1]
        area += xi * (yn - yp)
    area = abs(area)//2
    
    
    # Pickov teorem
    num_interior = area - num_points//2 + 1
    return num_interior + num_points



if __name__ == '__main__':
    fp = 'input.txt'
    p1(fp)
    p2(fp)