#kruskal 알고리즘 사용

def solution(n,costs):
    res=0
    costs.sort(key=lambda x:x[2])
    con=[costs[0][0]]

    while len(con) != n:
        for i, cost in enumerate(costs):
            if(cost[0] in con) and  (cost[1] in con):continue
            if (cost[0] in con) or (cost[1] in con):
                res +=cost[2]
                con.append(cost[0])
                con.append(cost[1])
                con = list(set(con))
                costs.pop(i)
                break
    return res


if __name__ == "__main__":
    n=4
    costs=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]