def solution(heights):
    answer = []

    for _ in range(len(heights)):
        x = heights.pop()
        i = len(heights) - 1
        check = True
        for _ in range(len(heights)):
            if (heights[i] > x):
                check = False
                answer.append(i + 1)
                break
            i = i - 1
        if (check == True):
            answer.append(0)
    answer.reverse()
    return answer

'''
def solution(h):
    ans = [0] * len(h)
    for i in range(len(h)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                ans[i] = j+1
                break
    return ans
'''