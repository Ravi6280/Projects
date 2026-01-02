#Project 1 : Hangman
#source Code:-

import random as ran
def hangman():
    word_list=['apple','sweat','likes','india','treat','phone']
    word = ran.choice(word_list)
    
    turns=5
    guessmade=''
    guess=''
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')
    
    while(len(word)>0):
        
        main_word=''
  
        for letter in word:                       
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "
                
    
        if main_word== word:                          
            print(main_word)
            print("congratulations you won !!")
            break
            
        if guess not in word:                          
            turns = turns-1
            if turns ==4:
                print("4 turns left")
                print("_______\n"
                      "|      \n"
                      "|      \n"
                      "|      \n"
                      "|      \n"
                      "|      \n"
                      "|      \n"
                     )
                
            if turns ==3:
                print("3 turns left")
                print("_______\n"
                      "|     |\n"
                      "|      \n"
                      "|      \n"
                      "|      \n"
                      "|      \n"
                      "|      \n"
                     )
            
            if turns ==2:
                print("2 turns left")
                print("_______\n"
                      "|     |\n"
                      "|     |\n"
                      "|      \n"
                      "|      \n"
                      "|      \n"
                      "|      \n"
                      
                     )
            if turns ==1:
                print("1 turns left")                
                print("_______\n"
                      "|     |\n"
                      "|     |\n"
                      "|     |\n"
                      "|      \n"
                      "|      \n"
                      "|      \n"
                     )
            if turns ==0:
                print("_______\n"
                      "|     |\n"
                      "|     |\n"
                      "|     |\n"
                      "|     O\n"
                      "|    /|\ \n"
                      "|    / \ \n"
                     )
                print("No turns left!")
                print("you lost the game")
                break
                
    
        print("make a guess ",main_word)
        
        guess=input()                               
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("not valid \n enter again")
            guess=input()
            
            
print("welcome to hangman !")
print("start game by pressing y or yes")
n=input()
n=n.lower()
if n=='y' or n=='yes':
    hangman()
else:
    "Game Ended"

