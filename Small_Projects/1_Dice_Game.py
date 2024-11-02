import random, time

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

#instanciate a class into local object
dice = Dice()
time.sleep(0.5)
first_count = 0
second_count = 0
draw = 0

#start the game
print("Let's start the game.")
for i in range(1, 5):
    first_value, second_value = dice.roll()
    print(f"First Number: {first_value},Second Number: {second_value}")

    #check conditions
    if first_value > second_value:
        print("First is greater.\n")
        first_count += 1

    elif second_value > first_value:
        print("Second is greater\n")
        second_count += 1

    else:
        print("First and Second are equal.\n")
        draw += 1

    time.sleep(1)


print(f"First won {first_count} times.")
print(f"Second won {second_count} times.")
print(f"Match draw {draw} times.")
time.sleep(1)

#Declare the winner
if first_count > second_count:
    print("First is the WINNER.")

elif second_count > first_count:
    print("Second is the WINNER.")

elif first_count == second_count:
    print("Match is DRAW.")
