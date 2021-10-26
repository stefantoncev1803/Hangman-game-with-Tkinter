import random
import os
import sys
import hangman_prints

words = ["apple", "pear", "apricot", "orange", "lemon", "watermelon", "grapes", "bannana", "kiwi"]
rand_word = random.choice(words)
first_list = []
a_list = first_list + ["_"] * len(rand_word)
print(a_list)
moves = 5
moves_2 = 5


def check_winner():
    a_string = ''.join(a_list)
    if a_string == rand_word:
        return True


def check_words(player):
    # moves = 10
    for i in range(0, len(rand_word)):
        if rand_word[i] == player:
            a_list[i] = player
            continue
    for i in range(0, len(rand_word)):
        if rand_word[i] == player:
            return True


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


while (moves > 0) or (moves_2 > 0):
    while True:
        player_one = input("1st player Enter a letter: ").lower()
        check_words(player_one)
        if player_one.isalpha() == False:
            print("Please enter only a letter: ")
            restart_program()

        elif check_words(player_one) == True:
            print("You've guessed")
            print(a_list)
            check_winner()
            if (check_winner() == True):
                print("First player wins!")
                sys.exit(0)
        # moves-=1
        if check_words(player_one) != True:
            print("wrong!")
            print(a_list)
            moves -= 1
            print("Remaining moves: ", moves)
            if moves == 4:
                hangman_prints.first_print()
            elif moves == 3:
                hangman_prints.second_print()
            elif moves == 2:
                hangman_prints.third_print()
            elif moves == 1:
                hangman_prints.fourth_print()
            elif moves == 0:
                hangman_prints.fifth_print()
                print("First player lost, second player wins! ")
                sys.exit(0)
            break

    while True:
        player_two = input("2nd player Enter a letter: ").lower()
        check_words(player_two)
        if player_two.isalpha() == False:
            print("Please enter only a letter: ")
            restart_program()
        elif check_words(player_two) == True:
            print("You've guessed")
            print(a_list)
            check_winner()
            if (check_winner() == True):
                print("Second player wins!")
                sys.exit(0)

        if check_words(player_two) != True:
            print("wrong!")
            print(a_list)
            moves_2 -= 1
            print("Remaining moves: ", moves)
            if moves_2 == 4:
                hangman_prints.first_print()
            elif moves_2 == 3:
                hangman_prints.second_print()
            elif moves_2 == 2:
                hangman_prints.third_print()
            elif moves_2 == 1:
                hangman_prints.fourth_print()
            elif moves_2 == 0:
                hangman_prints.fifth_print()
                print("Second player lost, first player wins! ")
                sys.exit(0)
            break
