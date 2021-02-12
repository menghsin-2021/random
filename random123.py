import random

ra = random.randint(1, 100)

while True:
    rd = input('猜個1-100 的數字吧: ')
    rd = int(rd)

    if rd >= 1 and rd <= 100:
        if rd > ra:
            print('比答案大!')
        elif rd < ra:
            print('比答案小!')
        else:
            print('終於答對了')
            break
    else:
        break
