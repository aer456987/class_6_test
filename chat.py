# 讀取檔案
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
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

# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')

# (main)主要function
def main():
    import os
    file_name = 'input.txt'      # 檢查檔案是否存在
    if os.path.isfile(file_name):
        print('檔案存在。\n----------')
    else:
        print('檔案不存在')
    lines = read_file(file_name)
    lines = covert(lines)
    write_file('output.txt', lines)

main()