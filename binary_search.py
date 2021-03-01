def op(x):
    left = -1
    right = n
    while right > left + 1:
        middle = (left + right) // 2
        if a[middle] >= x:
            right = middle
        else:
            left = middle
    return right