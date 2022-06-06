def solution(str):
    if len(str) % 2 != 0:
        str = str + '_'
    arr = []
    for x in range(len(str)):
        if (x + 1) % 2 == 0:
            arr.append(str[x-1] + str[x])
    return arr