
name=input('enter your name:')

if name=='kiran':
    print('u r name is satisfied')
    password=int(input('enter your password:'))
    if password==1234:
        print('your password is correct')
        if name=='kiran' and password==1234:
            print('login successfully')
        else:
            print('please try again')
    else:
        print('you have entere wrong password')

else:
    print('login failed')