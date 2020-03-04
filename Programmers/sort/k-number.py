
def solution(arr,c):
    res=[]

    for i in range(len(c)):
        x,y=c[i][0],c[i][1]
        tmp=[]
        for j in range(x-1,y,1):
            tmp.append(arr[j])

        tmp.sort()
        res.append(tmp[c[i][2]-1])

    return res





array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))