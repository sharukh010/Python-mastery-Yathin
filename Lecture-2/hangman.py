import random 
words = ["apple","banana","carrot"]
misses = 0 
hangman = [
    "platform",#1
    "vertical pole",#2
    "horizontal pole",#3 
    "rope",#4 
    "head",#5
    "body",#6
    "left hand",#7 
    "right hand",#8
    "left leg",#9
    "right leg"#10 
]
word = random.choice(words)
length = len(word)
guess = ["_"for i in range(length)]
while True: 
    print("Guess: "," ".join(guess))
    print("Hangman: ",hangman[:misses])
    if misses >= 10:
        print("Hangman, is dead")
        print("Game over") 
        break 
    # _ _ _ _ _ _ 
    character = input("Enter your guess: ")
    if character in word: 
        pass # this block is not implemented yet 
    else: 
        misses = misses+1 
