def dic_flie():
    dic = {
        'tomato': '番茄',
        'apple': '蘋果'
    }
    while True:
        print('指令: 顯示所有字典(all)；新增資料(n)；離開(q)')
        user_input = input('輸入要查詢的字: ')
        if user_input == 'all':    # 顯示所有資料
            print(dic)
        elif user_input == 'n':    # 新增資料
            new_key = input('輸入key: ')
            new_value = input('輸入value: ')
            dic.setdefault(new_key, new_value)
            print('新增完成！')
        elif user_input == 'q':    # 離開
            break
        elif user_input in dic:
            print(dic[user_input])
        elif user_input not in dic:
            print('［找不到資料。］')
        
        print('==============')
    return dic
dic_flie()