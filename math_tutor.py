# юзер обирає скільки він хоче питань
#  даємо питання з можливістю ввести відповідь на кожне питання
#   коли всі відповіді є принт:
#   - дякую за участь
#   - кількість правильних\тотал
#   - відсоток правильності

# бонус 1
# виміряти кількість секунд який зайняло відповідь на кожне питання і в загальному

# бонус 2
# дати юзеру можливість обрати наскільки будуть складними питаннями (2*2 или 22*23)

# бонус 3
# показати всі питання з відповідями

questions_easy = {
    "2 × 2?": "4",
    "3 + 5?": "8",
    "10 - 4?": "6",
    "6 × 3?": "18",
    "20 ÷ 4?": "5",
    "7 + 8?": "15",
    "15 - 9?": "6",
    "4 × 5?": "20",
    "18 ÷ 3?": "6",
    "9 + 6?": "15",
    "11 - 7?": "4",
    "5 × 6?": "30",
    "24 ÷ 6?": "4",
    "13 + 4?": "17",
    "16 - 8?": "8",
    "3 × 7?": "21",
    "30 ÷ 5?": "6",
    "12 + 9?": "21",
    "14 - 6?": "8",
    "8 × 2?": "16",
}
questions_hard = {
    "12 × 8?": "96",
    "144 ÷ 12?": "12",
    "17 + 58?": "75",
    "200 - 73?": "127",
    "9²?": "81",
    "√64?": "8",
    "15% out of  200?": "30",
    "7 × 13?": "91",
    "256 ÷ 16?": "16",
    "45 + 78?": "123",
    "1000 - 364?": "636",
    "6³?": "216",
    "√121?": "11",
    "25% out of  480?": "120",
    "11 × 11?": "121",
    "3⁴?": "81",
    "500 ÷ 25?": "20",
    "99 + 99?": "198",
    "50% out of  750?": "375",
    "18 × 5?": "90",
}

import random, time

correct = 0
totl_time = 0
questions = {}


level = input("Chose the level (easy or hard): ").strip().lower()


if level == "hard":
    questions = questions_hard
elif level == "easy":
    questions = questions_easy
else:
    print("Invalis input,'easy' selected by default")
    questions = questions_easy
among = int(input("How many questions? "))
selected = random.sample(list(questions.items()), among)

for quest, answ in selected:
    print(quest)
    start = time.time()
    answer = input("Your answer: ")
    end = time.time()
    elapsed = round(end - start, 2)
    totl_time += elapsed
    print(f"You`ve answered for {elapsed} seconds")
    if answer.strip() == answ:
        correct += 1

print(f"---Congrats---\nIt`s time for review!")
print(f"You got: {correct} out off {among}\nPercent: {round(correct / among * 100)}%")
print(f"Time: {totl_time}")
print("-------All questions with answers-------")
for quest, answ in list(questions.items()):
    print(f"{quest} = {answ}")
