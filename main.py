def solution(str):
    if len(str) % 2 != 0:
        str = str + '_'
    return [(str[x-1] + str[x]) for x in range(len(str)) if (x + 1) % 2 == 0]