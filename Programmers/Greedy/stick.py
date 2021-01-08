def solution(name):
    arr=[min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    n,res=0,0

    while True:
        res=res+arr[n]
        arr[n]=0

        if sum(arr)==0: break
        l,r = 1,1

        while arr[n - l] == 0: l = l + 1
        while arr[n + r] == 0: r = r + 1

        res += l if l < r else r
        n += - l if l < r else r

    return res






if __name__ == "__main__":
    name="JEROEN"
    print(solution(name))
