def solution(clothes):
    arr = {}

    for i in clothes:
        arr[i[1]] = 0
    for i in clothes:
        arr[i[1]] = arr[i[1]] + 1

    sum = 1
    for i in arr.keys():
        sum = sum * (arr[i] + 1)

    return sum-1

'''
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
'''
