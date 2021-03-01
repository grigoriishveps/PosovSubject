from sum_big_number import start_sum

def binary_search(array, val):
    left = 0
    right = len(array)
    while right > left + 1:
        middle = (left + right) // 2
        if array[middle] >= val:
            right = middle
        else:
            left = middle
    return right
# Press the green button in the gutter to run the script.
def start_binary():
    a = list(map(int, input().split()))
    x = int(input())
    print(binary_search(a,x))
if __name__ == '__main__':
    # start_sum()
    start_binary()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
