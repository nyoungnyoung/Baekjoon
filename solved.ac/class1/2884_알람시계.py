# H, M : 시간, 분
# 24시간 표현 사용, 하루의 시작은 0:0, 끝은 23:59
# 불필요한 0은 사용하지 않는다
# 주어진 시간보다 45분 전의 시간 출력
# M >= 45 : M - 45
# else : H - 1 / M + 15
#   if H = -1 : H = 23

H, M = map(int,input().split())
if M >= 45:
    M -= 45
else:
    H -= 1
    M += 15
    if H == -1:
        H = 23

print(f'{H} {M}')