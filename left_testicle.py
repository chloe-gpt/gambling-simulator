import random

# Bonus and letter options
bonuses = ["WIN", "FUN", "FLY", "ABC", "AAA", "DIE", "ASS", "AOL", "HIT",
           "BRO", "BET", "TIT", "SCP", "WHY", "BOP", "BEE", "BUM", "ZAP",
           "DEW", "MUM", "HAG", "WTF", "PBS", "POO"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
           "Y", "Z"]


# Get random letters for spinning
def get_letters(luck) -> list:
    a = letters[random.randint(0, 25)]
    b = a if random.randint(1, round(15 - luck)
                            ) == 1 else letters[random.randint(0, 25)]
    if random.randint(1, 4) == 1:
        c = a if random.randint(1, round(15 - luck)
                                ) == 1 else letters[random.randint(0, 25)]
    else:
        c = b if random.randint(1, round(15 - luck)
                                ) == 1 else letters[random.randint(0, 25)]
    return [a, b, c]


# Calculate reward based on spin outcome and bet
def calculate_reward(spin: list, bet: int) -> int:
    double = False
    triple = False
    bonus = False
    reward = bet
    unique_letters = []

    for letter in spin:
        if letter not in unique_letters:
            unique_letters.append(letter)
        else:
            if spin.count(letter) == 3:
                triple = True
            else:
                double = True

    for bonus_word in bonuses:
        if f"{spin[0]}{spin[1]}{spin[2]}" == bonus_word:
            bonus = True

    if double:
        reward *= 2
    elif triple:
        reward *= 4
    if bonus:
        reward *= 4
    if not double and not triple and not bonus:
        reward = 0

    return reward

d = 1

l = 0

pc = 250

deez = []

for i in range(250):
    pc = 250
    d = 1
    bet = 1 + i
    while True:
        spin = get_letters(l)
        pc -= bet
        r = calculate_reward(spin, bet)
        pc += r
        if pc <= 0:
            break
        else:
            d += 1
    print(f"D{bet} =", d)
    deez.append(d)

print(deez)