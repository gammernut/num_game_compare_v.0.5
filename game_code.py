import random


def guessing_game():
    player_guess_num = -1
    the_number = random.randint(0, 100)
    # for player_guess_num in range(1, 7):
    # while player_guess_num != the_number:
    for player_guess_taken in range(0, 7):
        try:
            player_guess_text = input('please enter a number between 1 and 100 \n')
            player_guess_num = int(player_guess_text)
            if player_guess_num > the_number:  # > greater then
                print(f'your guess of {player_guess_num} is too high')
            elif player_guess_num < the_number:  # < less then
                print(f'your guess of {player_guess_num} is to low')
            else:
                break
        except ValueError:
            print('please enter a number. ')
    if player_guess_num == the_number:
        print(f'correct! the number was {the_number}!')
        # print('Thanks for playing')
    else:
        print(f'\nNope. The Number I was thinking of was {the_number}\n')

    print(f'you took {player_guess_taken} guesses.\n')
    print('play again?')
