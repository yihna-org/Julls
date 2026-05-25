# Старт — гравець має 1000 монет
# У мішку 10 кульок: 6 зелених + 4 червоних (після кожного раунду кулька повертається назад).
# Перед кожним раундом — гравець вводить суму ставки
# Випадково витягується кулька
# Показати результат раунду
# Кількість раундів — змінна (гравець сам вирішує скільки грати)
# Якщо монет < 500 → гра зупиняється автоматично

# Витягнув зелену+ ставка (виграв)
# Витягнув червону− ставка (програв)
# Залишилось менше 500 монетГра закінчена (втратив половину)

# Бонус
# Замінити 2 звичайні кульки на спеціальні:
# 🖤 Чорна (замість 1 зеленої) → виграш ×10 від ставки
# 🤍 Біла (замість 1 червоної) → програш ×5 від ставки
import random

point = 1000
balls = [
    "green",
    "green",
    "green",
    "green",
    "green",
    "White",
    "red",
    "red",
    "red",
    "Black",
]
bet = 0
ball_sampl = ""
print(f"Welcome!\nYou start the game with {point} gold pieces")
rounds = int(input("How much rouds do you want? "))
while rounds != 0:
    if point > 500:
        bet = int(input("Enter your bet: "))
        rounds -= 1
        ball_sampl = random.choice(balls)
        print(f"Random ball - {ball_sampl}")
        if ball_sampl == "green":
            point += bet
            print(f"Congrats! Your points: {point}")
        elif ball_sampl == "red":
            point -= bet
            print(f"Next time! Your points: {point}")
        elif ball_sampl == "White":
            point += bet * 10
            print(f"WOW! Your points: {point}")
        elif ball_sampl == "Black":
            point -= bet * 5
            print(f"Upss.. Your points: {point}")
    else:
        break
print(f"---Finish---\nYour final score:{point}")
