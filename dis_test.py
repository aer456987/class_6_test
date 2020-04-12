while True:
	user_input = input("輸入要查詢的字: ")
	dis = {
	'tomato': '番茄',
	'apple': '蘋果'
	}
	if user_input == 'q':
		break
	elif user_input in dis:
		print(dis[user_input])
	elif user_input not in dis:
		print('［找不到資料。］')