print("                                      WELLCOME TO")
print('''
           *     *  (        )     *       )                    *     *  (        )     *       )
        )     (    ) )   *    (  (|              *             )     (    ) )   *    (  (|              *
       (   *  )   (  (|  )  ) )  *      )                   (   *  )   (  (|  )  ) )  *      )
       * ) (      ( |   )  )  (| (( )  )               * ) (      ( |   )  )  (| (( )  )
          _    _                                         
         | |  | |                                        
         | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
         |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
         | |  | | (_| | | | | (_| | | | | | | (_| | | | |
         |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                              __/ |                      
                             |___/                       
       * ) (      ( |   )  )  (| (( )  )                * ) (      ( |   )  )  (| (( )  )
       (   *  )   (  (|  )  ) )  *      )                (   *  )   (  (|  )  ) )  *      )
        )     (    ) )   *    (  (|              *       )     (    ) )   *    (  (|              *
           *     *  (        )     *       )                   *     *  (        )     *       )

                    ''')
stages = ['''
  _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |      / \
  |       
 /|\
/_|_\
''', '''
    _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |      / 
  |       
 /|\
/_|_\
''', '''
     _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |       
  |       
 /|\
/_|_\
''', '''
   _______
  |/      |
  |      (_)
  |      \|
  |       |
  |       
  |       
 /|\
/_|_\ ''', '''
   _______
  |/      |
  |      (_)
  |       |
  |       |
  |       
  |       
 /|\
/_|_\
      ''', '''
     _______
  |/      |
  |      (_)
  |       
  |       
  |       
  |       
 /|\
/_|_\
''', '''
    _______
  |/      
  |       
  |       
  |       
  |       
  |       
 /|\
/_|_\
''']
import random
word_list = ['abruptly','absurd','abyss','avenue','awkward','beekeeper', 'bikini', 'blitz', 'blizzard', 'bookworm', 'buffalo', 'buffoon', 'buzzing', 'buzzwords', 'cobweb', 'cockiness', 'crypt', 'cycle', 'dizzying', 'dwarves', 'embezzle', 'equip', 'faking', 'fishhook', 'fixable', 'flopping', 'fluffiness','flyby', 'frizzled', 'funny', 'galaxy', 'gossip', 'icebox','injury', 'jackpot', 'jawbreaker', 'jaywalk', 'jelly', 'jogging', 'joking', 'joyful', 'juicy', 'kiwifruit', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'microwave', 'nightclub', 'nowadays', 'quiz', 'quizzes', 'rhythm', 'unworthy', 'unzip', 'uptown',  'vaporize', 'vodka', 'voodoo', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'whiskey', 'wimpy', 'witchcraft', 'wizard', 'youthful', 'yummy', 'zigzag','zombie','apple', 'ball', 'cat', 'dog', 'egg', 'fish', 'goat', 'hat', 'ice', 'jam','kite', 'lamp', 'moon', 'nest', 'orange', 'piano', 'queen', 'rain', 'star','tree', 'umbrella', 'van', 'whale', 'xylophone', 'yarn', 'zebra', 'cake','doll', 'frog', 'grape', 'horse', 'igloo', 'jelly', 'key', 'lion', 'mouse','nut', 'octopus', 'pizza', 'quilt', 'rose', 'sun', 'tiger', 'uncle', 'vase',
'water', 'x-ray', 'yogurt', 'zip' ]
chosen_word = random.choice(word_list)
lives = 6
n = len(chosen_word)
display=[]
for i in range(n):
    display.append('_')
print(display)
guessed_letters = []
letter_found = False # Initialize the flag outside the loop
while '_' in display:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"************************* You've already guessed {guess}! **************************")
    else:
        guessed_letters.append(guess)
        if guess in chosen_word:
            for i in range(n):
                if chosen_word[i] == guess:
                    display[i] = guess
                    letter_found = True  # Set the flag to True if the letter is found

            if letter_found:  # Print the celebration only if the flag is True
                print(f''' 
                  *     *   (     *       )       *  (      *     * 
                *     )    (  )  (  (  ( ) )(    * ) )    (     *   
                 + = ) ()  &&* {guess.upper()} IS IN THE WORD.*&)*(+ *) *
                      ) *  ) )    (   ( |     * ( ) *  ) (   (     * 
                ''')
                print(display)
            letter_found = False # Reset the flag for the next guess
        else: 
            lives -= 1
            print(stages[lives])
            print(f"                                   unfortunatly {guess.lower()} was NOT in the word                ")
            print(f"                                          You have {lives} lives remaining                         ")
            if lives == 0:
                print("                                                      You lose !!                                 ")
                print('''
 *  *       *  * 
*      *   *      *
*       * *       *
 *       *       *   
   *           *
     *       *
       *   *
        * *             
         *

                ''')
                break
if '_' not in display:
    print("                                               You Win !!!")
    print('''    

 __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)

     *     *   (     *       )       *  (      *     *    
 *     )    (  )  (  (  ( ) )  (    * ) )    (     *   
       ) *  ) )    (   ( |     * ( ) *  ) (   (     * 

      ''')
        
        



    

    




     


