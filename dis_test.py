dic = {
	'tomato': '番茄',
	'apple': '蘋果'
}
while True:
	user_input = input('輸入要查詢的字(輸入q離開): ')
	if user_input == 'q':
		break
	elif user_input in dic:
		print(dis[user_input])
	elif user_input not in dic:
		print('［找不到資料。］')
		user_ins = input('r=重新查詢/n=新增資料: ')
		if user_ins == 'r':
			continue
		elif user_ins == 'n':
			new_key = input('輸入key: ')
			new_valur = input('輸入valur: ')
			dis.setdefault(new_key, new_valur)
			print('新增完成！')