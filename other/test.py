from typing import List
def multiply(num1: List[int], num2: List[int]) -> List[int]:
    res = []
    start_x, x = 0, 0
    
    for i,a in enumerate(num1):
        
        for j,b in enumerate(num2):
            x = start_x
            if i == 0:
                res.append(a*b)
            else:
                if j < len(num2)-1:
                    res[x] += (a*b)
                else:
                    res.append(a*b)
            x += 1

        start_x += 1
    
    # print(res)
    carry_over = 0
    for i in range(len(res)-1,-1,-1):
        
        if carry_over: res[i] += carry_over
        if res[i] > 9:
            carry_over = int(res[i]/10)
            res[i] = res[i] % 10
            if i == 0:
                res.insert(0,carry_over)
        else:
            carry_over = 0
    # print(res)
    return res

a = [1,3,1]
b = [2,3]

multiply(a,b)