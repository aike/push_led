import mido
from mido import Message
import time

# フォントのグリフ定義
# 各要素は1（ON）または0（OFF）を示す
glyph = [
    [0,0,0,0,0,0,0,0  ,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0  ,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0  ,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0  ,1,1,1,0,1,0,1,0,0,1,1,0,0,1,1,0],
    [0,0,0,0,0,0,0,0  ,1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,0  ,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1],
    [0,0,0,0,0,0,0,0  ,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1],
    [0,0,0,0,0,0,0,0  ,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,1]
]

outport = mido.open_output('Ableton Push 2 Live Port')

# MIDIノート番号の基点、ベロシティ、チャンネルの設定
base_note = 36   # ノート番号36からスタート
channel = 0      # チャンネル0

alen = len(glyph[0])
for n in range(alen * 4):
    print(n)

    color = n // alen
    # print(color)
    # 8x8の各ピクセルに対して、左下から右下へ行優先でMIDIノート番号を割り当て
    for row in range(8):
        for col in range(8):
            col2 = (col + n) % alen
            note = base_note + ((7 - row) * 8 + col)
            if glyph[row][col2] == 1:
                v = 127 - color
                outport.send(Message('note_on', note=note, velocity=v))
            else:
                outport.send(Message('note_on', note=note, velocity=0))
    time.sleep(0.3)

# 送信済みのノートに対してノートオフメッセージを送信
for row in range(8):
    for col in range(8):
        note = base_note + ((7 - row) * 8 + col)
        outport.send(Message('note_on', note=note, velocity=0))

