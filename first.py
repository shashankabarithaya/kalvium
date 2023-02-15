import random
import os

# a function that reads the highest score of a given player from a file
def read_highest_score(player_name):
    if os.path.exists(player_name + '.txt'):
        with open(player_name + '.txt', 'r') as file:
            return int(file.read().strip())
    else:
        return 0

# a function that updates the highest score of a given player in a file
def update_highest_score(player_name, score):
    with open(player_name + '.txt', 'w') as file:
        file.write(str(score))

# a function that determines the winner of a Rock Paper Scissors round
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

# the main function that lets the player play the game
def play_game():
    print('Welcome to Rock Paper Scissors!')
    player_name = input('Enter your name: ')
    highest_score = read_highest_score(player_name)
    print(f'Your highest score is {highest_score}')

    while True:
        print('Choose your move: (rock, paper, scissors)')
        player_choice = input().lower()
        while player_choice not in ['rock', 'paper', 'scissors']:
            print('Invalid choice. Please enter rock, paper, or scissors.')
            player_choice = input().lower()

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f'Computer chooses {computer_choice}.')

        winner = determine_winner(player_choice, computer_choice)
        if winner == 'player':
            print('You win!')
            highest_score += 1
            update_highest_score(player_name, highest_score)
        elif winner == 'computer':
            print('Computer wins!')
        else:
            print("It's a draw!")

        print(f'Your current score is {highest_score}.')
        play_again = input('Do you want to play again? (y/n)').lower()
        if play_again != 'y':
            print('Thanks for playing!')
            break

if __name__ == '__main__':
    play_game()
