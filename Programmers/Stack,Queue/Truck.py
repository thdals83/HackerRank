import queue

def solution(bridge_length, weight, truck_weights):
    answer = 0
    clon=truck_weights.copy()
    final=[]
    ing=[]
    timeset=[]

    while True:
        if(final==clon):return answer+1

        if(len(truck_weights)!=0):
            if(sum(ing)+truck_weights[0]<=weight):
                ing.append(truck_weights.pop(0))
                timeset.append(0)

        for i in range(len(timeset)):
            timeset[i] = timeset[i] + 1

        if(len(timeset)!=0):
            if(timeset[0]==bridge_length):
                final.append(ing.pop(0))
                timeset.pop(0)

        answer=answer+1




bridge_length=100
weight=100
truck_weights=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print(solution(bridge_length, weight, truck_weights))