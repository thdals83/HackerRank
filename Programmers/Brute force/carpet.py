
def solution(brown, yellow):
    x=((brown+4)+((brown+4)**2-16*(brown+yellow))**0.5)/4
    y=(brown+yellow)//x
    x=int(x)
    y=int(y)
    return [max(x,y),min(x,y)]



if __name__=="__main__":
    a,b=map(int,input().split())
    print(solution(a,b))