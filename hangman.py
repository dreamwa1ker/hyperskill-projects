import random
#aaafff
won = 0
lost = 0


def menu():
    global won
    global lost
    print("H A N G M A N\n")
    option = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")

    if option == "play":
        play()
    elif option == "results":
        results()
    elif option == "exit":
        won = 0
        lost = 0
        exit()

def play():
    attempts = 8
    word = list(random.choice(('python', 'java', 'swift', 'javascript')))
    mask = list("-" * len(word))
    guesses = set()
    global won
    global lost

    while attempts and mask != word:

        print("".join(mask))
        guess = input("Input a letter: ")

        if guess in guesses:
            print("You've already guessed this letter.")
            continue
        elif not len(guess) == 1:
            print("Please, input a single letter.")
            continue
        elif not ord("a") <= ord(guess) <= ord('z'):
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        guesses.add(guess)

        if guess not in set(word):
            print("That letter doesn't appear in the word.")
            attempts -= 1
        elif guess in mask:
            print("No improvements.")
            attempts -= 1
        else:
            for i in range(len(word)):
                if guess == word[i]:
                    mask[i] = word[i]

    if mask == word:
        print(f"You guessed the word " + "".join(word) + "!" + "\nYou survived!")
        won += 1
    else:
        print("\nYou lost!")
        lost += 1
    menu()


def results():
    global won
    global lost
    print(f"You won: {won} times.")
    print(f"You lost: {lost} times.\n")
    menu()


menu()
