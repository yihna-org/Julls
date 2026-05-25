# LoyaltyPointsEngineChallenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)
purchases = []


def earn_points(price):
    whole_dollar = int(price)
    return whole_dollar * 3


"""
Convert a purchase amount into whole-dollar points.
Each dollar = 3 pts. Fractions of a dollar are ignored.
"""


def tier_label(points):
    if points >= 500:
        return "Gold"
    elif points >= 100:
        return "Silver"
    else:
        return "Bronze"


"""Return the loyalty tier name based on total points."""

total_spent = 0.0
total_points = 0

for amount in purchases:
    total_spent += amount
    total_points += earn_points(amount)

final_tier = tier_label(total_points)

print("---Loyalty Summary---")

print(
    f"Total dollars spent: {total_spent}\nTotal points earned: {total_points}\nFinal tier: {final_tier}\nCongratulations!!!"
)
