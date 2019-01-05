def binary_search(searchList, item):
    low = 0
    high = len(searchList)-1

    while low <= high:
        mid = int( (low+high)/2 )
        guess = searchList[mid]

        if guess == item:
            return True
        if guess > item:
            high = mid-1
        else:
            low = mid+1

    return False