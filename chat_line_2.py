# 讀取檔案
def read_file(file_name):
	with open(file_name, 'r', encoding='utf-8') as f:
		lines = []
		for line in f:
			lines.append(line.strip())
		# print(lines)
		return lines

# 轉換格式
def convert(lines):
	new = []
	for line in lines:
		s = line.split(' ')
		time = s[0][]
		name = s[0][5:]
		other = s[1:]
		print(name, ': ' , other)
	return new

def main():
	file_name = '[LINE]input_2.txt'
	lines = read_file(file_name)
	lines = convert(lines)


main()