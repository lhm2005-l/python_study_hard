# word_list 내부의 요소들 중 하나를 임의로 선택하기 위해 random모듈을 도입 (import)
'''
사용 예시

number = [1,2,3,4,5]
chosen_numbers = random.choise(numbers)
'''

#todo - 1 : word_list에서 단어 하나를 임의적으로 선택하도록 random 모듈을 사용하고, 해당 단어를 chosen_word라는 변수에 담으시오
#todo - 2 :  사용자에게 알파벳을 하나 추측해서 입력하라고 요청하고, 이를 guess변수에 담으시오, 그리고 대문자로 입력하는 경우를 방지하기 위해 input() 함수 뒤에 .lower()을 적용하시오.
#todo - 3 : guess에서 입력한 문자 하나가 chosen_word의 string문자열 중에 하나의 문자와 일치하는지를 반복문을 통해 확인할 수 있도록 프로그램을 작성하시오. (맞으면 정답, 틀리면 오답이라고 출력되게 만들것)
import random

word_list = ["apple', 'bannana", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("알파벳을 하나만 입력하세요 >>> ").lower()

# 향상된 for문
for i in chosen_word:
    if chosen_word in i:
        print("정답")
    else:
        print("오답")

# # 일반 for문
# for i in range(len(chosen_word)):
#     if guess == chosen_word[i]:
#         print("정답")
#     else:
#         print("오답")