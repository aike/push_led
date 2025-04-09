# midoを使用するバージョン
import mido
from mido import Message
import random
import time

font = [[ 
# A
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0]
],[
# B
    [1,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
],[
# C
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
],[
# D
    [0,0,0,0,0,0,0,0],
    [1,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
],[
# E
    [0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,1,1,0,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0]
],[
# F
    [0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,1,1,0,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0]
],[
# G
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,0,1,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
],[
# (blank)
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
],[
# b
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,1,0],
    [0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
],[
# #
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,1,1,0],
    [0,0,0,0,0,1,1,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
],[
# m
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0]
],[
# M7
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,1,0,0,1],
    [0,0,0,1,1,1,0,1]
],[
# 7
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,1]
],[
# 9
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,1]
],[
# dim
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1],
    [0,0,0,0,0,1,0,1],
    [0,0,0,0,0,1,1,1]
],[
# half dim
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1],
    [0,0,0,0,0,1,1,1],
    [0,0,0,0,0,1,1,1]
],[
# aug
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,1,1,1],
    [0,0,0,0,0,0,1,0]
]]

chordpos = {
    "M":    [[0,0],[-1,1],[2,1]],
    "m":    [[0,0],[3,0],[2,1]],
    "M7":   [[0,0],[-1,1],[2,1],[1,2]],
    "m7":   [[0,0],[-2,1],[-3,2],[0,2]],
    "7":    [[0,0],[-1,1],[-3,2],[0,-1]],
    "dim":  [[0,0],[3,0],[1,1]],
    "aug":  [[0,0],[-1,1],[-2,2]],
    "hdim": [[0,0],[3,0],[1,1],[0,2]],
}    

notepos = {
    "C":  [2,2],
    "C#": [3,2],
    "D":  [4,2],
    "D#": [5,2],
    "E":  [1,3],
    "F":  [2,3],
    "F#": [3,3],
    "G":  [4,3],
    "G#": [5,3],
    "A":  [1,4],
    "A#": [2,4],
    "B":  [3,4],
}

black = 0
white = 122
lightgray = 123
darkgray = 124
blue = 125
green = 126
red = 127


debug = False


def font_copy(font_a):
    return [row[:] for row in font_a]

def font_or(font_a, font_b):
    result = [[font_a[i][j] | font_b[i][j] for j in range(8)] for i in range(8)]
    return result

def make_font(base, mod1, mod2):
    index = ord(base) - ord("A")
    result = font_copy(font[index])
    if mod1 == "":
        result = font_or(result, font[7])
    elif mod1 == "b":
        result = font_or(result, font[8])
    elif mod1 == "#":
        result = font_or(result, font[9])
    
    if mod2 == "M":
        result = font_or(result, font[7])
    elif mod2 == "m":
        result = font_or(result, font[10])
    elif mod2 == "m7":
        result = font_or(result, font[10])
        result = font_or(result, font[12])
    elif mod2 == "m9":
        result = font_or(result, font[10])
        result = font_or(result, font[13])
    elif mod2 == "M7":
        result = font_or(result, font[11])
    elif mod2 == "7":
        result = font_or(result, font[12])
    elif mod2 == "9":
        result = font_or(result, font[13])
    elif mod2 == "dim":
        result = font_or(result, font[14])
    elif mod2 == "hdim":
        result = font_or(result, font[15])
    elif mod2 == "aug":
        result = font_or(result, font[16])

    return result     

if not debug:
    outport = mido.open_output('Ableton Push 2 Live Port')

def midi_put(x, y, color):
    note = 36 + ((7 - y) * 8 + x)
    outport.send(Message('note_on', note=note, velocity=color))

def midi_clear():
    for y in range(8):
        for x in range(8):
            note = 36 + ((7 - y) * 8 + x)
            outport.send(Message('note_on', note=note, velocity=black))

def text_put(x, y, s):
    # ANSIエスケープシーケンス: ESC [ {行};{列} H
    print(f"\033[{y * 1 + 1};{x * 2 + 1}H{s}", end="")

def text_clear():
    # ANSIエスケープシーケンス: ESC [ 2 J
    print("\033[2J", end="")



def put(x, y, color):
    if debug:
        if color == 0:
            text_put(x, y, "..")
        elif color == 1:
            text_put(x, y, "$$")
        elif color == 2:
            text_put(x, y, "[]")
        elif color == 3:
            text_put(x, y, "##")
        elif color == 4:
            text_put(x, y, "@@")
    else:
        if color == 0:
            midi_put(x, y, black)
        elif color == 1:
            midi_put(x, y, blue)
        elif color == 2:
            midi_put(x, y, darkgray)
        elif color == 3:
            midi_put(x, y, lightgray)
        elif color == 4:
            midi_put(x, y, green)

def clear():
    if debug:
        text_clear()
    else:
        midi_clear()


def show(data8x8):
    for y in range(8):
        for x in range(8):
            put(x, y, data8x8[y][x])
    if debug:
        print("")

def show_scale():
    data = [ 
        [2,3,0,2,0,2,2,0],
        [0,2,0,2,0,2,3,0],
        [0,2,0,2,2,0,2,0],
        [0,2,0,2,3,0,2,0],
        [0,2,2,0,2,0,2,0],
        [0,2,3,0,2,0,2,2],
        [2,0,2,0,2,0,2,3],
        [3,0,2,0,2,2,0,2]
    ]
    clear()
    show(data)


def next_question(base, mod1, mod2):
    # 1. ランダムにコードを選択
    # base = random.choice(["C", "D", "E", "F", "G", "A", "B"])
    # mod1 = ""
    # mod2 = random.choice(["M", "m", "M7", "m7", "7", "dim", "aug", "hdim"])

    pos = notepos[base + mod1]

    # 2. コードネームを表示
    clear()
    show(make_font(base, mod1, mod2))
    time.sleep(1.5)

    # 3. スケールを表示
    show_scale()
    time.sleep(0.5)

    # 4. コードを表示
    chord = chordpos[mod2]
    for i in range(len(chord)):
        cpos = chord[i]
        x = pos[0] + cpos[0]
        y = pos[1] + cpos[1]
        if x > 5:
            x -= 5
            y += 1
        elif x < 1:
            x += 5
            y -= 1        
        if y > 5:
            x += 3
            y -= 3
        put(x, 7 - y, 4)
    if debug:
        print("")
    time.sleep(3)

for i in range(8):
    next_question("E", "", "m7")
    next_question("A", "", "m7")
    next_question("D", "", "m7")
    next_question("G", "", "7")

    # next_question("C", "", "M7")
    # next_question("D", "", "m7")
    # next_question("G", "", "7")

    show_scale()
