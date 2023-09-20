import random as r

guesses = []


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def print_line(guess, random_number):
    print('Your guesses were: ')
    for i in bubble_sort(guesses):
        if i == guess:
            print('(', i, ')', end=', ')
        elif i == random_number:
            print('You should guess here', end=', ')
        else:
            print(i, end=", ")
    print('')


def main():
    print('A simple number guessing game using bubble sort.')
    diff = int(input("Choose a number that will be the upper boundary of the randomness: "))
    tries_og = int(input('Choose number of tries: '))
    tries = tries_og
    random_number = r.randrange(0, diff)
    guesses.append(random_number)
    print(f'The number you must guess is in range 0 to {diff}')
    while True:
        print(f'You have {tries} tries left')
        try:
            guess = int(input('Input your number: '))
        except ValueError:
            print('You must enter a number, try again')
            continue
        if random_number == guess:
            tries -= 1
            print(f'You win, the number was {random_number}. You guessed it in {tries_og - tries} tries')
            try:
                score = (diff ** 1.3) // tries_og * (tries_og - tries) ** 1.5
                print('Your score is : ', score)
            except ZeroDivisionError:
                print('You guessed it in 0 tries, no score can measure your skill')
            break
        elif guess > random_number:
            tries -= 1
            guesses.append(guess)
            print('Too large')
            print_line(guess, random_number)
        elif guess < random_number:
            tries -= 1
            guesses.append(guess)
            print('Too small')
            print_line(guess, random_number)
        if tries == 0:
            print(f'You lost, the number was {random_number}')
            break


if __name__ == '__main__':
    main()
