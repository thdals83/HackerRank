def solution(participant, completion):
    dic={}

    for i in participant:
        dic[i]=dic.get(i,0)+1

    for i in completion:
        dic[i]=dic[i]-1

    for i in dic.keys():
        if(dic[i]!=0):
            return i

'''
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''

'''
'''