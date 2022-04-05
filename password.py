password = 'a123456'
i = 3
while i > 0:
    i = i - 1 
    word = input('please input password: ')
    if word == password:
        print('correct password!')
        break
    else:
        print('wrong password')
        if i > 0:
            print('you have ', i, 'chances')
        else:
            print('your account is locked')
