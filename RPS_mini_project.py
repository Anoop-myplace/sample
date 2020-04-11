import random

print("<===== It's a Rock Paper Scissor Game =====>")
ucount,ccount = 0,0

while True:
    
    while True:
        print("\n1. Rock\n2. Paper\n3. Scissor\n")
        user_choice = input("Please Enter your Choice :  ")
        user_choice = user_choice.lower()
        if user_choice not in ['rock','paper','scissor']:
            print("Please enter a valid choice")
        else: break
    
    print("Your choice is : {}".format(user_choice))
    
    cmp_choice = random.choice(['rock','paper','scissor'])
    print("\nComputer's  choice is : {}".format(cmp_choice))
    
    print("\t"+user_choice+"\n (V/S)\n\t"+cmp_choice+"\n")
    result = None
    
    if ((user_choice=='rock' and cmp_choice=='scissor') or 
       (cmp_choice=='scissor' and user_choice=='rock')):
        result = 'rock'
    elif ((user_choice=='paper' and cmp_choice=='rock') or 
       (cmp_choice=='rock' and user_choice=='paper')):
        result = 'paper'
    elif ((user_choice=='scissor' and cmp_choice=='rock') or 
           (cmp_choice=='rock' and user_choice=='paper')):
        result = 'rock'
    elif ((user_choice=='rock' and cmp_choice=='paper') or 
           (cmp_choice=='paper' and user_choice=='rock')):
        result = 'paper'
    else: 
        result = 'scissor'
    
    
    if (user_choice == cmp_choice):
        print("<===== Draw =====>")
    elif (user_choice == result):
        print("<===== You Win =====>")
        ucount += 1
    else : 
        print("<===== Computer win's =====>")
        ccount += 1
    
    ans = input("Do you want to play again? Y/N : ")
    
    if(ans == 'n' or ans == 'N'):
        break

if(ucount > ccount):
    print("******   Congradualtion You have won this Game with {} points  ******".format(ucount))
else:
    print("******   You lost this game by {} points   ******".format(ccount-ucount))
    print("******   Better Luck Next Time   ******")
    
print("\nThanks for Playing this Game")
