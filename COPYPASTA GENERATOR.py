''' 
Finding the password is too easy if you know Python
(Thanks senpai Sam Miller for noticing this piece of crap)
'''


__okayu__ = 'MOGU MOGU OKAYU!!!'
__korone__ = 'YUBI YUBI'


def okakoro_reward():
    thing_want = input('I want to get... ')
    char_limit = input('Do you have a character limit? (Y/N): ')
    line_per_item = input('Do you want a line per item? (Y/N): ')
    if char_limit == 'N':
        char = input('I want this much of it (A NUMBER PLEASE): ')
        if line_per_item == 'Y':
            for char in range(0, int(char)):
                print(str(thing_want))
        if line_per_item == 'N':
            for char in range(0, int(char)):
                print(str(thing_want), end="")
    if char_limit == 'Y':
        char_num = input('How many characters can you write? ')
        actual_char_num = int(char_num) // len(thing_want)
        if line_per_item == 'Y':
            for actual_char_num in range(0, int(actual_char_num)):
                print(str(thing_want))
        if line_per_item == 'N':
            for actual_char_num in range(0, int(actual_char_num)):
                print(str(thing_want), end="")


def okakoro_pass():
    x = input('What\'s the password? ')
    if str(x) == 'MOGU MOGU OKAYU!!!' or str(x) == 'YUBI YUBI~' or str(x) == 'a':
        print('YOU ENTERED THE CORRECT PASSWORD! You can get any amount of anything you want')
        okakoro_reward()
    else:
        print('Found the impostor, AH↓ HA↑ HA↑ HA↑')


if __okayu__ == 'MOGU MOGU OKAYU!!!' and __korone__ == 'YUBI YUBI~':
    print('Welcome to OkaKoro!')
    okakoro_reward()
else:
    okakoro_pass()
