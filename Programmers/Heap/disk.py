import heapq

def solution (j):
    j.sort()
    res=0
    time=0
    arr=[]
    n=len(j)
    num=len(j)

    while num!=0:
        for _ in range(len(j)):
            if (time >= j[0][0]):
                heapq.heappush(arr, (j[0][1], j[0][0]))
                j.pop(0)
            else:break

        if arr:
            tmp = list(heapq.heappop(arr))
            res = res + (abs(time - tmp[1]) + tmp[0])
            time = time + tmp[0]

            num = num - 1

        else: time = time + 1

    return int(res/n)


if __name__=="__main__":
    jobs = [[0, 3], [1, 9], [2, 6]]

    print(solution(jobs))