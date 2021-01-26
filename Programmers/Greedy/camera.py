def solution(routes):
    res=0
    routes.sort(key=lambda x:x[1])
    x= -30001

    for route in routes:
        if x < route[0]:
            res+=1
            x=route[1]

    return res

# 효율성 테스트 통과 못함
"""
def solution(routes):
    res=1
    routes.sort(key=lambda x:x[1])
    check=routes[0][1]

    print(check,routes)

    for i in range(1,len(routes)):
        if routes[i][0]<check<routes[i][1]:
            continue
        else:
            res += 1
            check=routes[i][1]

    return res
"""



if __name__=="__main__":
    routes=[[-20,15], [-14,-5], [-18,-13], [-5,-3]]
    print(solution(routes))