def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            temp=phone_book[j]
            if (phone_book[i]==temp[:len(phone_book[i])]):
                return False

    return True
