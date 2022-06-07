def solution(InputText):
    InputText += '_'
    return [(InputText[x-1] + InputText[x]) for x in range(len(InputText)) if (x + 1) % 2 == 0]