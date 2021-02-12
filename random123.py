import random

start = input('請決定最小值: ')
end = input('請決定最大值: ')
start = int(start)
end = int(end)

ra = random.randint(start, end)
count = 0
while True:
    count += 1 # count = count + 1
    rd = input('猜個你自己決定範圍的數字吧: ')
    rd = int(rd)

    if rd >= start and rd <= end:
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
        print('輸入在自己設定的範圍內好嗎')
        break
