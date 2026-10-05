import random 
words = ["apple","banana","carrot"]
misses = 0 
fill = 0 
# hangman = [
#     "platform",#1
#     "vertical pole",#2
#     "horizontal pole",#3 
#     "rope",#4 
#     "head",#5
#     "body",#6
#     "left hand",#7 
#     "right hand",#8
#     "left leg",#9
#     "right leg"#10 
# ]
hangman = [
"""





/=====\\
""",
"""
   + 
   |
   |
   |
   |
/=====\\
""",
"""
   + ---------+
   |
   |
   |
   |
/=====\\
""",
"""
   + ---------+
   |          |
   |
   |
   |
/=====\\
""",
"""
   + ---------+
   |          |
   |          O
   |
   |
/=====\\
""",
"""
   + ---------+
   |          |
   |          O
   |          |
   |
/=====\\
""",
"""
   + ---------+
   |          |
   |          O
   |         /|
   |
/=====\\
""",
"""
   + ---------+
   |          |
   |          O
   |         /|\\
   |
/=====\\
""",
"""
   + ---------+
   |          |
   |          O
   |         /|\\
   |         /
/=====\\
""",
"""
   + ---------+
   |          |
   |          O
   |         /|\\
   |         / \\
/=====\\
""",

]
word = random.choice(words)
length = len(word)
guess = ["_"for i in range(length)]
"""
"banana"
 012345
 b,_,_,_,_,_
 0 1 2 3 4 5
 b _ _ _ _ _  
"""
while True: 
    print("Guess: "," ".join(guess))
    if misses != 0: 
        print("Hangman: \n",hangman[misses-1])
    else:
        print("Hangman: \n")
    if fill == length: 
        print("Game over")
        print("You won")
        break 
    if misses >= 10:
        print("Hangman, is dead")
        print("Game over") 
        break 
    # _ _ _ _ _ _ 
    character = input("Enter your guess: ").lower()
    start = -1 
    if character in word: 
        # pass # this block is not implemented yet 
        count = word.count(character)
        while count > 0: 
            # print(count)
            start = word.index(character,start+1)
            guess[start] = character
            fill += 1 
            count -= 1 
    else: 
        misses = misses+1 
