def solution(Inputstr):
    Inputstr += '_'
    return [(Inputstr[x-1] + Inputstr[x]) for x in range(len(Inputstr)) if (x + 1) % 2 == 0]