def solution(N, number):

    if N == number:return 1

    arr=[set() for i in range(8)]

    for i,j in enumerate(arr,start=1):
        j.add(int(str(N) * i))

    for i in range(1,8):
        for j in range(i):
            for op1 in arr[j]:
                for op2 in arr[i-j-1]:
                    arr[i].add(op1 + op2)
                    arr[i].add(op1 - op2)
                    arr[i].add(op1 * op2)
                    if op2 != 0: arr[i].add(op1 // op2)

        if number in arr[i]:
            res=i+1
            break

    else:
        res=-1

    return res



if __name__ =="__main__":
    N=5
    number=12
    print(solution(N, number))
