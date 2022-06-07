def solution(Input_string):
    Input_string += '_'
    return [(Input_string[x-1] + Input_string[x]) for x in range(len(Input_string)) if (x + 1) % 2 == 0]