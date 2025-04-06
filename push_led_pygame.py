import pygame
import pygame.midi
import time

# pygame と pygame.midi の初期化
pygame.init()
pygame.midi.init()

# MIDI出力デバイスIDを取得
for dev in range(pygame.midi.get_count()):
    info = pygame.midi.get_device_info(dev)
    if info[1].decode() == 'Ableton Push 2' and info[3] == 1:
        output_id = dev
        break

# MIDI出力デバイスをオープン
midi_out = pygame.midi.Output(output_id)
print(midi_out)

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


# MIDIノート番号の基点、ベロシティ、チャンネルの設定
base_note = 36   # ノート番号36からスタート
channel = 0      # チャンネル0

try:
    alen = len(glyph[0])
    for n in range(alen * 4):
        print(n)

        color = n // alen
        print(color)

        # 8x8の各ピクセルに対して、左下から右下へ行優先でMIDIノート番号を割り当て
        for row in range(8):
            for col in range(8):
                col2 = (col + n) % alen
                note = base_note + ((7 - row) * 8 + col)
                if glyph[row][col2] == 1:
                    midi_out.note_on(note, 127 - color, channel)
                else:
                    midi_out.note_on(note, 0, channel)
        time.sleep(0.3)

    # 送信済みのノートに対してノートオフメッセージを送信
    for row in range(8):
        for col in range(8):
            note = base_note + ((7 - row) * 8 + col)
            midi_out.note_on(note, 0, channel)

except Exception as e:
    midi_out.close()
    pygame.midi.quit()
    pygame.quit()


# 後処理：MIDI出力デバイスをクローズし、pygame.midi と pygame を終了
midi_out.close()
pygame.midi.quit()
pygame.quit()
