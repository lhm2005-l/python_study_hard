
'''
업그레이드 관련 지시사항

1. chrome에서 사이트를 확인한 후 bmi가 특정 구간일 때마다
 당신의 bmi지수는 xx.xx이고, 저체중/정상/과체중/비반입니다.가 출력될 수 있돟록
 조건문 작성
'''

height = float(input("당신의 키는 몇 cm입니까? >>>")) / 100
weight = float(input("단신의 몸무게는 몇 kg 입니까? >>>"))
bmi = weight / (height ** 2)   # 반복적으로 나오게 되는 연산의 경우에는 간단한 변수열에 대입하는 것이 가졷성이 높은 코드를 작성하는 방식에 해당
bmi = round(bmi,2)
if bmi >= 18.5:
    print(f'당신의 bmi지수는 {bmi}이고, 저체중입니다.')
elif 18.5 < bmi <= 23:
    print(f'당신의 bmi지수는 {bmi}이고, 정상입니다.')
elif 23 < bmi <= 25:
    print(f'당신의 bmi지수는 {bmi}이고, 과체중입니다.')
else:
    print(f'당신의 bmi지수는 {bmi}이고, 비만입니다.')