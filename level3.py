import random

guessesTaken = 0 

print('Hello!?! What is your name?!?!')
myName = input()

print('Well,' + myName + ', pick a number between 1 and 10.')
myNumber = input()
myNumber = int(myNumber)

while guessesTaken < 3: 
    print('Computer takes a guess')
    guess = random.randint(1, 10)
    print(guess)

    guessesTaken = guessesTaken + 1

    if guess < myNumber:
        print('Your guess is too low.')

    if guess > myNumber:
        print('your guess is too high.')
    
    if guess == myNumber:
        break

if guess == myNumber:
    guessesTaken = str(guessesTaken)
    print('Oh no, ' + myName + '! The computer guessed your number in ' + guessesTaken +' guesses!')

if guess != myNumber:
    myNumber = str(myNumber)
    print('Winner Winner CHICKEN DINNER. The number I was thinking of was ' + myNumber)

#On level three, the computer's guesses are optimized to refine the range on the guesses
# based on whether they are too high or too low. 
# Print how many guesses it takes the computer before it correctly guesses the number.