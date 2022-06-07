def solution(inputText):
    inputText += '_'
    return [(inputText[x-1] + inputText[x]) for x in range(len(inputText)) if (x + 1) % 2 == 0]