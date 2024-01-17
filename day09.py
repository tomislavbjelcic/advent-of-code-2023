import numpy as np

    
def solution(fp):
    front = []
    back = []
    
    with open(fp) as f:
        
        for line in f:
            hist = []
            line = line.strip()
            nums = list(map(int, line.split()))
            nums = np.array(nums, dtype=np.int32)
            diff = nums
            while (diff!=0).any():
                hist.append(diff)
                diff = diff[1:] - diff[:-1]
            hist.append(diff)
            hist.reverse()
            
            interpolated = [0]
            for i in range(1,len(hist)):
                aa = hist[i][-1] + interpolated[i-1]
                interpolated.append(aa)
            front.append(interpolated[-1])
            
            
            interpolated = [0]
            for i in range(1,len(hist)):
                aa = hist[i][0] - interpolated[i-1]
                interpolated.append(aa)
            back.append(interpolated[-1])

    print(sum(front))
    print(sum(back))
    




if __name__ == '__main__':
    fp = 'input.txt'
    solution(fp)
    