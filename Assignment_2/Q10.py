import random  # used to generate random dice number

def guess_the_dice():
    dice = [1, 2, 3, 4, 5, 6]  # possible dice values
    target = random.choice(dice)  # actual dice result

    try:
        # user guess input
        a = int(input("Roll your dice. Guess the outcome \n >"))
    except ValueError:
        # handle invalid input
        print("(;﹏;)")
        return

    # difference between guess and actual value
    difference = abs(a - target)

    # check accuracy of guess
    if difference == 0:
        print("(^_^)")
    elif difference == 1:
        print("((-_-))")
    else:
        print("(;﹏;)")

def main():
    # run the game
    guess_the_dice()

if __name__ == "__main__":
    main()