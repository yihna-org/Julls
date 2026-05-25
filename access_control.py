#  Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

revoke_badge = {5251, 2852, 8592}
approved = []
denied = []

while True:
    name = input("Enter your name (or type 'done' to finish): ")

    if name.lower() == "done":
        break
    else:
        badge = int(input("Enter your badge number: "))

        if badge in revoke_badge:
            print("ACCESS DENIED")
            denied.append(name)
        else:
            print("ACCESS GRANTED")
            approved.append(name)

approved.sort()
denied.sort()

print("---Access Summary---")

print(
    f"✅ {len(approved)} Approved Visitors - {approved}\n"
    f"⛔️ {len(denied)} Denied Visitors - {denied}"
)
