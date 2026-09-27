question1 = "what is 2+2?"
question2 = "what is capital of Italy?"
question3 = "which programming langugae yathin knows?"
question4 = "what is the best online multiplayer game?"
question5 = "what is the capital of India?"
answer1 = "2+2 is 4."
answer2 = "capital of Italy is Rome"
answer3 = "yathin knows python programming language"
answer4 = "minecraft is the online multiplayer game"
answer5 = "Capital of India is Delhi"
print("Chat Bot: V1")
while True: 
    prompt = input("Prompt: ")
    if prompt == question1: 
        print(f"Response: {answer1}")
    elif prompt == question2: 
        print(f"Response: {answer2}")
    elif prompt == question3: 
        print(f"Response: {answer3}")
    elif prompt == question4: 
        print(f"Response: {answer4}")
    elif prompt == question5: 
        print(f"Response: {answer5}")
    else:
        print("Response: Sorry, couldn't answer the question.")