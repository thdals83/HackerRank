import heapq

def solution(s,k):
    if(len(s)==1):
        if(s[0]>=k):return 0
        else:return -1

    elif((len(s))==2):
        if(s[0]>=k and s[1]>=k):return 0
        res=s[0]+(s[1]*2)
        if(res>=k): return 1
        else: return -1
    count = 0
    heapq.heapify(s)

    while True:
        if(len(s)>=3):
            if(s[0]>=k):return count
            else:
                count=count+1
                x=heapq.heappop(s)
                y=heapq.heappop(s)
                heapq.heappush(s,x+(y*2))
        elif(len(s)==2):
            if (s[0] >= k and s[1] >= k): return count
            count = count + 1
            x = heapq.heappop(s)
            y = heapq.heappop(s)
            heapq.heappush(s, x + (y * 2))
            if(s[0]<k):return -1


if __name__=="__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    k = 7

    print(solution(scoville,k))