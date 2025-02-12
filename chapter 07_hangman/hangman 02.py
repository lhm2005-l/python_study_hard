import random

word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
guess = input("알파벳을 하나만 입력하세요 >>> ").lower()

#todo - 1 : 비어있는 list인 display를 만드시오, chosen_sord의 각 문자 개수마다 "_"를 추가하시오. (chosen_word == "apple"이라면, display = ["_","_","_","_","_"]이 되어야 함. 문자의 개수 만큼  "_"가 생김)
#todo - 2 : chosen_word의 각 문자를 반복시키세요, 만약 그 위치의 문자가 guess와 일치하면 해당 위치의 display에서 해당 문자를 공개하세요 (사용자가 "p"를 입력했고, chosen_word가 "apple"이라면 display = ["_",p,p,"_","_"])

# 일반 for문
display = []
for _ in range(len(chosen_word)):             # 변수가 사용되지 않으므로 i가 아니라 _로 명시됨.
    display.append("_")


# # 나
# for letter in range(len(chosen_word)):
#     display.append("_")
#     if guess in letter:
#         display[guess] = letter
# print(display)

# 선생님
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess

print(display)