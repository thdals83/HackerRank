def solution(genres,plays):
    d = {}
    playsDict = {}

    x = 0
    for i, j in zip(genres, plays):
        playsDict[i] = playsDict.get(i, 0) + j
        d[i] = d.get(i, []) + [(j, x)]
        x = x + 1
    print(d)
    arr = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)
    print(arr)
    res = []
    for i in range(len(arr)):
        arr2 = sorted(d[arr[i][0]], key=lambda x: x[0], reverse=True)
        if(len(arr2)==1):res.append(arr2[0][1])
        else:
            res.append(arr2[0][1])
            res.append(arr2[1][1])

    return res


genres=	["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]

solution(genres,plays)

'''
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
'''