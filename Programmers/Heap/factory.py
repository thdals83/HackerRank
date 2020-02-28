import heapq

def solution(stock, dates, supplies, k):
    res = 0
    rag = 0
    pq = []

    while stock < k:
        for i in range(rag, len(dates)):

            if stock < dates[i]: break
            heapq.heappush(pq, -supplies[i])
            rag = i + 1

        stock =stock + (heapq.heappop(pq) * -1)

        res=res+1

    return res



if __name__=="__main__":
    stock=4
    dates = [4,10,15]
    supplies = [20,5,10]
    k=30

    print(solution(stock, dates, supplies, k))