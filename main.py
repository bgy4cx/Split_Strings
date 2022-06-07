def solution(Input_str):
    Input_str += '_'
    return [(Input_str[x-1] + Input_str[x]) for x in range(len(Input_str)) if (x + 1) % 2 == 0]