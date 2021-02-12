import random

ra = random.randint(1, 100)
count = 0
while True:
    count += 1 # count = count + 1
    rd = input('猜個1-100 的數字吧: ')
    rd = int(rd)

    if rd >= 1 and rd <= 100:
        if rd > ra:
            print('比答案大!')
        elif rd < ra:
            print('比答案小!')
        else:
            print('終於答對了')
            print('這是你猜的第', count, '次')
            break
        print('這是你猜的第', count, '次')
    else:
        break
