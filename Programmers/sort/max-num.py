def solution(num):
    arr=[]
    num=list(map(str,num))

    arr=sorted(num,key=lambda x:x*3,reverse=True)
    res=str(''.join(arr))

    return res



numbers = [3, 30, 34, 5, 9]
print(solution(numbers))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

'''
..
'''