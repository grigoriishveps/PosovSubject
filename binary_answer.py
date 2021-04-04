def check(array, l):
    m = 1
    s = l
    for i in range(1, len(array)):
        if (s >= array[i] - array[i-1]):
            s -= array[i] - array[i-1]
        else:
            s = l
            m += 1
    return m

def binary_search(array, k):
    left = -1
    right = array[-1] - array[0]
    while right > left + 1:
        middle = (left + right) // 2
        if check(array, middle) <= k:
            right = middle
        else:
            left = middle
    return right

def start_binary():
    n = int(input())
    a = [0]*n
    k = int(input())
    for i in range(n):
        a[i] = int(input())
    print(*a)
    print(binary_search(a, k))

if __name__ == '__main__':
    start_binary()