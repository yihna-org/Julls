# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

while True:
    phon_num = input("Enter UA phone number in any format (10 digits): ")
    phon_num = phon_num.strip()

    for chp in [
        "-",
        "(",
        ")",
        ".",
    ]:
        phon_num = phon_num.replace(ch, " ")
    phon_num = phon_num.split()
    phon_num = "".join(phon_num)

    if len(phon_num) == 10:
        print(f"Your number - ({phon_num[:3]}) {phon_num[3:]}")
        break
    else:
        print("Please enter exactly 10 digits.")
        continue
