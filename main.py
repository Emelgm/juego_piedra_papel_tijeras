import random

def welcome():
    print("""
            GAME START

    CHOOSE OPTION FOR START:

    [🪨] - ROCK 
    [📰] - PAPER
    [✂️] - SCISSORS

    """)


def choose_option():
    """
    Function to choose an option
    """
    list_option = ('ROCK', 'PAPER', 'SCISSORS')
    computer_option = random.choice(list_option).upper()
    user_option = input('\nChoose an option: ').upper()

    if not user_option in list_option:
        print('\nThe option is not valid')
        return None, None
    
    print(f'\nUSER OPTION: {user_option}')
    print(f'COMPUTER OPTION: {computer_option}')
    
    return user_option, computer_option


def process_option(user_option, computer_option, user_wins, computer_wins):
    """
    Function to process both options
    """
    if user_option == computer_option:
        print('\nEMPATE')
    elif user_option == 'ROCK' and computer_option == 'SCISSORS':
        print(f'\nThe USER win with {user_option}')
        user_wins += 1
    elif user_option == 'PAPER' and computer_option == 'ROCK':
        print(f'\nThe USER win with {user_option}')
        user_wins += 1
    elif user_option == 'SCISSORS' and computer_option == 'PAPER':
        print(f'\nThe USER win with {user_option}')
        user_wins += 1
    else:
        print(f'\nThe COMPUTER win with {computer_option}')
        computer_wins += 1
    
    return user_wins, computer_wins


def end():
    """
    Function to end or continue
    """
    restart =''
    while restart != 'x':
        restart = input('\n[Y]Continue or [X]exit\n:').upper()
        if restart == 'Y':
            run()
        elif restart == 'X':
            print('\n')
            print('×'*19)
            print('THE PROGRAM IS OVER')
            print('×'*19)
            restart = 'x'
            break
        else:
            print('The option is not valid')


def run():
    """
    Start function
    """
    welcome()
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('\n')
        print('-'*15)
        print(f'Round: {rounds}')
        print('-'*15)
        print(f'\nSCORE\nCOMPUTER: {computer_wins}\nUSER: {user_wins}')
        rounds +=1
        user_option, computer_option = choose_option()
        user_wins, computer_wins = process_option(user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print()
            print('*'*26)
            print(f'COMPUTER: {computer_wins} - {user_wins} :USER')
            print('\n¡¡The winner is COMPUTER!!')
            print('*'*26)
            break

        if user_wins == 2:
            print()
            print('*'*22)
            print(f'COMPUTER: {computer_wins} - {user_wins} :USER')
            print('\n¡¡The winner is USER!!')
            print('*'*22)
            break


if __name__=='__main__':
    run()
    end()