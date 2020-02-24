def solution(p,l):
    answer=0
    m=max(p)
    while True:
        v=p.pop(0)
        if m==v:

            answer=answer+1

            if l == 0 : break
            else: l = l-1
            m=max(p)

        else:
            p.append(v)

            if l==0: l=len(p)-1
            else: l=l-1

    return answer



if __name__=="__main__":
    p=[1,1,9,1,1,1]
    l=0

    print(solution(p,l))