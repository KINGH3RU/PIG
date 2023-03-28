#random sum of dice rolls 1-6
#hold swithces turns
#game stops and total is shown if you roll 1 or total >= 20
import random


def holdAt20():
    turnT = 0
    while turnT < 20:
        roll = random.randint(1,6)
        print("Roll:", roll)
        if roll == 1:
            turnT = 0
            print("Turn Total:", turnT)
            return turnT
        else:
            turnT += roll
    print("Turn Total:", turnT)
    return turnT
x = holdAt20()
print(x)


def HoldAt20Outcomes(trials):
    outcomes = {0:0}
    for val in range(20,26):
        outcomes[val] = 0
    for _ in range(trials):
        score = holdAt20()
        outcomes[score] +=1
    for score in outcomes:
        print(score, outcomes[score]/trials)



def holdAtLim(limit):
    turnT = 0
    while turnT < limit:
        roll = random.randint(1,6)
        print("Roll:", roll)
        if roll == 1:
            turnT = 0
            print("Turn Total:", turnT)
            return turnT
        else:
            turnT += roll
    print("Turn Total:", turnT)
    return turnT


def HoldAtXoutcomes(trials, limit):
    outcomes = {0:0}
    for val in range(limit,limit+6):
        outcomes[val] = 0
    for _ in range(trials):
        score = holdAtLim(limit)
        outcomes[score] +=1
    for score in outcomes:
        print(score, outcomes[score]/trials)
HoldAtXoutcomes(100,30)
