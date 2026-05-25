names = ["john ClEEse", "Eric IDLE", "michael"]
names1 = ["graHam chapman", "TERRY", "terry jones"]

gen_names = names + names1
gen_names.append(input(f"Enter your guest: "))
gen_names.append(input(f"One more: "))
print(gen_names)

for invites in gen_names:
    print(f"{invites.title()}! You are invited to the party on Saturday.")
