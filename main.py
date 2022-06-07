def solution(input_str):
    input_str += '_'
    return [(input_str[x-1] + input_str[x]) for x in range(len(input_str)) if (x + 1) % 2 == 0]