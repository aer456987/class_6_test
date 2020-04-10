# 讀取檔案
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
        return lines


# 計算數量
def covert(lines):
    a_word_count = 0
    a_sticker_count = 0
    a_image_count = 0
    v_word_count = 0
    v_sticker_count = 0
    v_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                a_sticker_count += 1
            elif s[2] == '圖片':
                a_image_count += 1
            else:
                for m in s[2:]:
                    a_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                v_sticker_count += 1
            elif s[2] == '圖片':
                v_image_count += 1
            else:
                for m in s[2:]:
                    v_word_count += len(m)
    print('A說了:', a_word_count, '個字,', a_sticker_count, '個貼圖和', a_image_count, '張圖片')
    print('V說了:', v_word_count, '個字,', v_sticker_count, '個貼圖和', v_image_count, '張圖片')


# 寫入檔案
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line[0] + ' ' + line[1] + ' ' + line[2:] + '\n')


# (main)主要function
def main():
    import os
    file_name = '[LINE]input.txt'      # 檢查檔案是否存在
    if os.path.isfile(file_name):
        print('檔案存在。\n----------')
    else:
        print('檔案不存在')
    lines = read_file(file_name)
    lines = covert(lines)
    #write_file('[LINE]output.csv', lines)
  
main()