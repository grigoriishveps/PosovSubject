from sum_big_number import start_sum

def binary_search(array, val):
    left = -1
    right = len(array)-1
    while right > left + 1:
        middle = (left + right) // 2
        if array[middle] >= val:
            right = middle
        else:
            left = middle
    print(right)
    if array[right] == val:
        return right
    return -1

def start_binary():
    #a = list(map(int, input().split()))
    x = 0
    while x!=-1:
        x = int(input())
        # a = [1, 2, 2, 4, 8, 8, 8, 10, 11, 12, 17, 18, 21]
        a = [1, 5, 9, 11, 20, 23, 30, 50, 93, 100]
        print(binary_search(a, x))
if __name__ == '__main__':
    # start_sum()
    start_binary()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
