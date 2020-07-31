from itertools import permutations

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
        print(a)

    a -= set(range(0, 2))

    print(int(max(a) ** 0.5))
    for i in range(2, int(max(a) ** 0.5) + 1):
        print(i)
        a -= set(range(i * 2, max(a) + 1, i))
        print(a)
    print(a)
    return len(a)

if __name__=="__main__":
    print(solution("011"))


'''
from itertools import permutations

def solution(s):
    answer = 0

    new_s = list(s)
    for i in range(2,len(s)+1):
        pm = list(permutations(s, i))
        for j in pm:
            if len(j) <= len(s):
                new_s.append(''.join(j))
    new_s = list(set([int(x) for x in new_s]))
    
    if new_s.count(1):
        new_s.remove(1)
    if new_s.count(0):
        new_s.remove(0)

    for x in new_s:
        i = 2
        while i*i <= x: 
            if x % i == 0:
                answer -= 1
                break
            i+=1
        answer += 1
    
    return answer
'''