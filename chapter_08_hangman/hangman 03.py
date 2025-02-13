import random       # 특정 모듈을 사용한다는 것을 맨 처음에 명시함

'''
"".join(반복가능객체) method : . 앞에 있는 문자열을 기준으로 반복 가능 객체의 요소들을 합쳐서 str으로 반환함
'''
# temp = ["안", "녕", "하", "세", "요"]
# hello = "".join(temp)
# print(hello)
# print("/".join(temp))
# print("/ ".join(temp))

word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append("_")

while "_" in display:
    guess = input("알파벳을 하나만 입력하세요 >>> ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)

print(" ".join(display))
print("정답입니다!")