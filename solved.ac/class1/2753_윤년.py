# 연도가 주어졌을 때 윤년 : 1 / 아니면 : 0 출력
# 윤년 = 연도가 4의 배수이면서 100의 배수가 아닐 때, 혹은 400의 배수일 때
# 2012 = 4의 배수이면서 100의 배수가 아님. 윤년
# 1900 = 100의 배수이고 400의 배수는 아님. 윤년X
# 2000 = 400의 배수. 윤년
# 1번 조건 : 400의 배수? O : 윤년 / X : 2번 조건
# 2번 조건 : 100의 배수? O : 윤년X / X : 3번 조건
# 3번 조건 : 4의 배수? O : 윤년 / X : 윤년X

year = int(input())
if year % 400 == 0:
    print('1')
else:
    if year % 100 == 0:
        print('0')
    else:
        if year % 4 == 0:
            print('1')
        else:
            print('0')
