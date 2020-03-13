def create(x,ar,depth, tmp, visited):

    if (depth == x):
        x=('').join(tmp)
        x=int(x)
        num.append(x)
        return

    for i in range(len(ar)):
        if(visited[i]==False):
            visited[i]=True
            tmp.append(ar[i])
            create(x,ar,depth+1)
            visited[i]=False
            tmp.pop()

def confirm(array, n):
    list = [False, False] + [True] * (n - 1)
    index=[]
    count=0
    for i in range(2,n+1):
        if(list[i]==True):
            index.append(i)
            for j in range(2*i,n+1,i):
                list[j]=False

    for i in array:
        for j in index:
            if(i==j):
                count=count+1
                break

    return count

def solution(numbers):
    # answer = 0
    # x=input()
    arr = []
    tmp = []
    for i in numbers: arr.append(i)
    visited = [False] * len(arr)
    num = []
    for i in range(1, len(arr) + 1):
        create(i, arr, 0)






    num = set(num)
    num = list(num)
    max = max(num)
    # print(confirm(num,max))

    return confirm(num, max)
