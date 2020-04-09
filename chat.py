# 檢查檔案是否存在
import os
def os_ckeck():
    filename = 'input.txt'
    if os.path.isfile(filename):
        print('檔案存在。\n----------')
    else:
        print('檔案不存在')

# 讀取檔案
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
        return lines

# convert轉換格式
def covert(lines):
    new = []
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        new.append(person + ': ' + line)
    return new

def write_file(flilname, lines):
	with open(flilname, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')

# main主要function
def main():
    lines = read_file('input.txt')
    lines = covert(lines)
    write_file('output.txt', lines)

os_ckeck()
main()