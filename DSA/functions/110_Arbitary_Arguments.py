# Arbitary Arguments

def adder(*num):
    sum = 0
    for n in num:
        sum += n
    print(f"Sum: {sum}")

adder(1,2,3)
adder(2,3,4,5,6,7)
adder(12,23,45,45,1,4,2,3)