import random

CHOICES = ('r', 'p', 's')

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

def determine_winner(choice, computer_choice):
        if choice == computer_choice:
            print('Tie!')
        elif (choice == 'r' and computer_choice == 's') or (choice == 'p' and computer_choice == 'r') or (choice == 's' and computer_choice == 'p'):
            print('You won')
        else:
            print('You lose!')

def print_choices(choice, computer_choice) -> None:
    print(f'You chose {parse_to_emoji(choice)}')
    print(f'Computer chose {parse_to_emoji(computer_choice)}')

def keep_playing() -> bool:
    print('Continue? (y/n): ')
    choice = input().lower()
    while(choice != 'y' and choice != 'n'):
        print('Invalid option. Try again!')
        choice = input.lower()
    return choice == 'y'

def parse_to_emoji(choice : str) -> str:
    match choice:
        case 'r':
            return '\U0001FAA8'
        case 'p':
            return '\U0001F4C3'
        case 's':
            return '\U00002702'

def get_user_input(prompt : str) -> str:
    choice = input(prompt)
    while (choice.lower() not in CHOICES):
        print('Invalid choice. Try again!')
        choice = input(prompt)
    return choice
        
if __name__ == '__main__':
    main()