import random


def main():
    """
    Guessing game to guess a number, it will tell you higher and lower depending on your input
    :return:
    """
    print("Hello player, welcome to the GUESSING GAME")
    print("Youre going to choose if the number I chose for you is higher or lower, its between 1-100")
    print("Ready? Let's start")

    guess = random.randint(1, 100)
    choice = True

    def game(welcome):
        count = 0
        guessingint = int()
        while guessingint != welcome:
            guessingint = int(input("What number do you think I thought of?"))
            if count > 10:
                print("TOO MANY TRIES. YOU LOSE")
                choice = False
                break
            if guessingint < welcome:
                print("Higher")
                count += 1
                print(count)
            if guessingint > 100:
                print("Its between 1-100")

            elif guessingint > welcome:
                print("Lower")
                count += 1
                print(count)
        return guessingint
    game(welcome=guess)
    if choice:
        print(f"Youre right, it was the number {game(guess)}")


if __name__ == '__main__':
    main()
