def solution(a):
    n=[[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    r=[0,0,0]
    tmp=[0,0,0]


    for i in a:
        for j in range(3):

            if(n[j][tmp[j]]==i):
                r[j]=r[j]+1

        for k in range(3):
            if(tmp[k]==(len(n[k])-1)):
                tmp[k]=0
            else:
                tmp[k]=tmp[k]+1

    res=[]
    for i in range(3):
        if(r[i]==max(r)):
            res.append(i+1)

    return res


if __name__=="__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 3, 2, 4, 2]
    solution(arr2)