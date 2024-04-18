secret_num = 5
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    if(guess == secret_num):
        print('You Win! :)')
        break
    guess_count+=1
   
else:
    print('Failed to guess the right number :(')
