# n = int(input("정수 입력:"))
# if n >0:
#     print('양의 정수입니다')
# elif n == 0:
#     print('0입니다')
# else:
#     print('음의 정수입니다')
#
# # 영어 점수 입력, 등급산출
# s = int(input("영어 점수 입력:"))
# if 100>= s >=90:
#     print('1등급')
# elif 90 > s >=80:
#     print('2등급')
# elif 80> s >=70:
#     print('3등급')
# elif s >100:
#     print('ERROR')
# else:
#     print('재수강')
#
# #정수 입력, 음/양/0/짝/홀 구분
# n = int(input("정수 입력:"))
# if n >0 and n % 2 == 0:
#     print("양의 짝수")
# elif n >0 and n%2 == 1:
#     print("양의 홀수")
# if n <0 and n % 2 == 0:
#     print("음의 짝수")
# elif n <0 and n%2 == 1:
#     print("음의 홀수")
# if n == 0:
#     print("0")

#비밀번호 설정 입력받고, 8보다 적으면 재설정 요구하기
n = input("비밀번호 입력:")
if len(n) < 8 :
    print("재설정")
if '!' not in n:
    print("특수문자 미포함")
else:
    print("설정 완료")














