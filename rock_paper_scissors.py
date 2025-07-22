import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
EMOJIS = {ROCK: '\U0001FAA8', PAPER: '\U0001F4C3', SCISSORS: '\U00002702'}
CHOICES = tuple(EMOJIS.keys())


def main():
    rock_paper_scissors()

def rock_paper_scissors() -> None:
    prompt = 'Rock, paper, or scissors? (r/p/s): '
    playing = True
    while (playing):
        computer_choice = random.choice(CHOICES)
        choice = get_user_input(prompt)

        print_choices(choice, computer_choice)
        determine_winner(choice, computer_choice)

        playing = keep_playing()

    print('Thanks for playing :)')

def determine_winner(choice : str, computer_choice : str) -> None:
        if choice == computer_choice:
            print('Tie!')
        elif (
            (choice == ROCK and computer_choice == SCISSORS) or 
            (choice == PAPER and computer_choice == ROCK) or 
            (choice == SCISSORS and computer_choice == PAPER)):
            print('You won!')
        else:
            print('You lose!')

def print_choices(choice : str, computer_choice : str) -> None:
    print(f'You chose {EMOJIS[choice]}')
    print(f'Computer chose {EMOJIS[computer_choice]}')

def keep_playing() -> bool:
    print('Continue? (y/n): ')
    choice = input().lower()
    while(choice != 'y' and choice != 'n'):
        print('Invalid option. Try again!')
        choice = input.lower()
    return choice == 'y'

def get_user_input(prompt : str) -> str:
    choice = input(prompt)
    while (choice.lower() not in CHOICES):
        print('Invalid choice. Try again!')
        choice = input(prompt)
    return choice
        
if __name__ == '__main__':
    main()