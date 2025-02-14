import random
import hangman_word_list            # import 파일명
import hangman_arts

chosen_word = random.choice(hangman_word_list.word_list)        # 변수를 가져올땐 파일명.변수명

print(f"테스트 코드 : {chosen_word}")
display = []
for _ in range(len(chosen_word)):
    display.append("_")

print(hangman_arts.logo)
lives = 6

end_of_game = False
while not end_of_game:
    guess = input("알파벳을 하나만 입력하세요 >>> ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f"당신의 기회는 {lives}번 남았습니다")
        if lives == 0:
            print("모든 기회를 잃었습니다.")
            end_of_game = True
            print(f"정답은 {chosen_word}였습니다.")

    if "_" not in display:
        print("정답입니다!")
        end_of_game = True

    print(" ".join(display))
    print(hangman_arts.stages[lives])