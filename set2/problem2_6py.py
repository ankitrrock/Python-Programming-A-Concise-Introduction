import random

def problem2_6():
    random.seed(431)
    for roll in range(0,100):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(die1+die2)
