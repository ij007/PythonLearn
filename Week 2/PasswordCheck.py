password = str(input())

if(len(password)>=8 and len(password)<=32):
    if(password[0].isalpha()):
        if(not password.count('/') and not password.count('\\') and not password.count('=') and not password.count(',') and not password.count("'") and not password.count(' ') and not password.count('"')):
            print(True)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)