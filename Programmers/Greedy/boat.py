def solution(people, limit):
    people.sort()
    res=0;
    i=0;
    j=len(people)-1

    while i<=j:
        res=res+1
        if people[j]+people[i]<=limit:
            i=i+1
        j=j-1

    return res

if __name__ == "__main__":
    people = [70,50,80,50]
    limit = 100
    print(solution(people,limit))