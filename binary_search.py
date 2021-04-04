def binary_search(array, val):
    left = -1
    right = len(array)-1
    while right > left + 1:
        middle = (left + right) // 2
        if array[middle] >= val:
            right = middle
        else:
            left = middle
    if array[right] == val:
        return right
    return -1

def start_binary():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    for i in range(k):
        x = int(input())
        print(binary_search(a, x))

if __name__ == '__main__':
    start_binary()