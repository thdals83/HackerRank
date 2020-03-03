import heapq

def solution(op):
    arr=[]

    for i in range(len(op)):
        use=op[i].split(" ")
        if(use[0]=="I"):
            arr.append(int(use[1]))

        else:
            if(len(arr)!=0):
                if (use[1] == "1"):
                    arr.pop()
                else:
                    arr.pop(0)

        arr.sort()

    if(len(arr)==0):
        return [0,0]
    else:
        return [max(arr),min(arr)]


if __name__=="__main__":
    operations=["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))


