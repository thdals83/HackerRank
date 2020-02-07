def sockMerchant(n, ar):
    sum=0
    ar2=set(ar)

    for i in ar2:
        sum=sum+(ar.count(i)//2)

    return sum



if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)