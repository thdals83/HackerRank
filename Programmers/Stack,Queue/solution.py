def solution(p, s):
    answer = []

    while len(p)!=0:
        count=0
        for i in range(len(p)):
            p[i]=p[i]+s[i]

        while True:
            if(len(p)==0):break

            if(p[0]>=100):
                p.pop(0)
                s.pop(0)
                count=count+1
            else:break
        if (count != 0): answer.append(count)

    return answer


if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))