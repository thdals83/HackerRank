
def solution(n,lost,reserve):

    s_re=set(reserve)-set(lost)
    s_lo=set(lost)-set(reserve)

    for i in s_re:
        if i-1 in s_lo:
            s_lo.remove(i-1)
        elif i+1 in s_lo:
            s_lo.remove(i+1)

    res = n - len(s_lo)
    return res


if __name__=="__main__":
    n=5
    list=[2,4]
    reserve=[3]
    print(solution(n,list,reserve))
