def sum_big(first, second):
    if len(first) < len(second):
        first, second = second, first
    first = first[::-1]
    second = second[::-1]
    res = ""
    flag = 0
    for i in range(len(second)):
        k = int(first[i]) + int(second[i]) + flag
        flag = k // 10
        res += str(k % 10)
    else:
        pos = len(second)
        while(flag == 1 and pos < len(first)):
            k = int(first[pos]) + flag
            flag = k // 10
            res += str(k % 10)
            pos += 1
        else:
            if(pos == len(first) and flag == 1):
                res += "1"
        res += first[pos: len(first)]
    return res[::-1]


def start_sum():
    n = int(input())
    for i in range(n):
        first, second = input().split()
        res = sum_big(first, second)
        print(res)

if __name__ == '__main__':
    start_sum()
