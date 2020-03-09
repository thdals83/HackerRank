def solution(c):
    arr=sorted(c,reverse=True)

    for i in range(len(arr)):
        if(i>=arr[i]):return i

    return len(arr)






if __name__=="__main__":
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))