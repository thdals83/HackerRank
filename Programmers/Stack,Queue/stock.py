def solution(prices):
    save = []

    for i in range(len(prices) - 1):
        count = 0
        check = True
        for j in range(i + 1, len(prices)):
            count = count + 1
            if (prices[i] > prices[j]):
                save.append(count)
                check = False
                break

        if (check == True):
            save.append(count)

    save.append(0)

    return save


prices=	[1, 2, 3, 2, 3]
