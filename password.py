password = 'a123456'
i = 3
while True:
    word = input('please input password: ')
    if word != password:
        i = i - 1
        if i == 0:
            print('your account is locked')
            raise SystemExit
        else:
            print('wrong password, you have ', i, 'chances')
    else:
        print('correct password!')
        break