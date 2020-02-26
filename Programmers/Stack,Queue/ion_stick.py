def solution(a):
    a = a.replace('()', '0')

    res = 0
    x=0
    cnt=0

    for i in a:
        if (i == '('):
            x=x+1
            cnt=cnt+1

        elif (i == ')'):
            x=x-1

        else:
            cnt=cnt+x

    return cnt

if __name__=="__main__":
    x = "()(((()())(())()))(())"
