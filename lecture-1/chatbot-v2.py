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
print("Chat Bot: V2")
while True: 
    prompt = input("Prompt: ")
    if prompt.lower().replace(" ","") in question1.lower().replace(" ",""): 
        print(f"Response: {answer1}")
    elif prompt.lower().replace(" ","") in question2.lower().replace(" ",""): 
        print(f"Response: {answer2}")
    elif prompt.lower().replace(" ","") in question3.lower().replace(" ",""): 
        print(f"Response: {answer3}")
    elif prompt.lower().replace(" ","") in question4.lower().replace(" ",""): 
        print(f"Response: {answer4}")
    elif prompt.lower().replace(" ","") in question5.lower().replace(" ",""): 
        print(f"Response: {answer5}")
    else:
        print("Response: Sorry, couldn't answer the question.")