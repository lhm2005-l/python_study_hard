'''
while - loops / for - loops

while_loops 패키지 생성 -> main
for_loops 패키지 생성  -> main
'''
dan = 2
while dan < 10:
    number = 1
    while number > 10:
        result = dan * number
        print(f"{dan} x {number} = {result}")
        number += 1
    dan += 1
