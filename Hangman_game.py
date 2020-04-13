import random 

words = ['apple','banana','orange','coconut','strawberry','lime','grapes','lemon','kumquat','blueberry','melon']

while True:
    start = input("Press enter / return to start, or enter Q to quit : ")

    if start.lower() == 'q':
        break
    
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []
    
    while len(bad_guesses) < 4 and (len(good_guesses)) != len (list( secret_word)):
        count = 0
        for letter in secret_word:
            if letter in good_guesses:
                print ( letter , end='')
                count +=1
            else:
                print('_', end=' ')
                
        print('\nStrikes : {} / 4'.format(len(bad_guesses)))
        print ('')
        
        if count == len ( list(secret_word)):
            print ("You win : The word was {}". format(secret_word))
            break

        guess = input ("Guess a letter : ").lower()

        if  len(guess) != 1:
            print ("You can only guess a single letter !") 
            continue
        elif guess in bad_guesses :
            print("You have already guess that letter")
            continue
        elif not guess.isalpha():
            print ("You can only guess letters !")
            continue
        
        if guess in secret_word:
            good_guesses.append(guess)
        else:
            bad_guesses.append(guess)
              
    else:   
        print ("You didn't guess it: my secret word was {}". format(secret_word))

print("<================= Thank You for Playing this game ================>")