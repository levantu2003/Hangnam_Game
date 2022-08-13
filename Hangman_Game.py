import random

words = ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']

print(f'The words are {list}')

word = random.choice(words)
guesses = ''
turns = 10

print(f'You have {turn} turns to guess!')

while turns > 0:
    print(f'You have {turns} turns left!')
    guessed_all = True
    for c in word:
        if c in guesses:
            print(c, end = ' ')
        else:
            print('_', end = ' ')
            guessed_all = False
    print()
    if not guessed_all:
        guess = input('Guess the char: ')
        guesses = guess + guesses
        if guesses not in word:
            turns = turns - 1
            if turns == 0:
                print("Better luck next time!")
    else:
        turns = 0
        print('Congratulations. You win!')
