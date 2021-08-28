# -*- coding: utf-8 -*-

def solution(new_id):
    answer = ''
    allowed_spcstr = ['-', '_', '.']
    
    # 1단계
    id1step = new_id.lower()
    print("1step:", id1step)

    # 2단계
    id2step = ""
    for ch in id1step:
        # 숫자, 영문 대문자, 영문 소문자 여부 확인
        if ord(ch) in range(48,58) or ord(ch) in range(65,91) or ord(ch) in range(97,123):
            id2step = id2step + ch
        # 허용 특수문자 여부 확인
        if ch in allowed_spcstr:
            id2step = id2step + ch
    print("id2step:", id2step)

    # 3단계
    id3step = id2step
    while True:
        tmp = id3step.replace("..", ".")
        if tmp == id3step:
            break
        id3step = tmp
    print(id3step)

    # 4단계
    id4step = id3step
    if id4step

    return answer

solution("...!@BaT#*..y.abcdefghijklm")

# ord('-'): 45
# ord('.'): 46

# ord('0'): 48
# ord('9'): 57

# ord('A'): 65
# ord('Z'): 90

# ord('_'): 95

# ord('a'): 97
# ord('z'): 122
