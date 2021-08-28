# -*- coding: utf-8 -*-

def solution(new_id):
    allowed_spcstr = ['-', '_', '.']
    
    # 1단계
    id1step = new_id.lower()
    #print("1step:", id1step)

    # 2단계
    id2step = ""
    for ch in id1step:
        # 숫자, 영문 대문자, 영문 소문자 여부 확인
        if ord(ch) in range(48,58) or ord(ch) in range(65,91) or ord(ch) in range(97,123):
            id2step = id2step + ch
        # 허용 특수문자 여부 확인
        if ch in allowed_spcstr:
            id2step = id2step + ch
    #print("id2step:", id2step)

    # 3단계
    id3step = id2step
    while True:
        tmp = id3step.replace("..", ".")
        if tmp == id3step:
            break
        id3step = tmp
    #print("id3step:", id3step)

    # 4단계
    id4step = id3step

    if id4step[0] == '.':
        id4step = id4step[1:]
    if len(id4step) > 0:
        if id4step[-1] == '.':
            id4step = id4step[:-1]
    #print("id4step:", id4step)

    # 5단계
    id5step = id4step
    if len(id5step) == 0:
        id5step = "a"
    #print("id5step:", id5step)

    # 6단계
    id6step = id5step
    if len(id6step) >= 16:
        id6step = id6step[:15]
    if id6step[-1] == '.':
        id6step = id6step[:-1]
    #print("id6step:", id6step)

    # 7단계
    id7step = id6step
    if len(id7step) <= 2:
        while len(id7step) < 3:
            id7step += id7step[-1]

    #print("id7step:",id7step)
    return id7step

inputstr = "...!@BaT#*..y.abcdefghijklm"
#inputstr = "z-+.^."
#inputstr = "=.="
#inputstr = "123_.def"
#inputstr = "abcdefghijklmn.p"

solution(inputstr)
