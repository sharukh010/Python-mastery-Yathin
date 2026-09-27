"""
"what is 2+2 ?"
"what is 2+2?"


remove all the spaces 

whatis2+2?
whatis2+2?
"""

prompt = "what is      2+2      ?"
question = "what is 2+2?"
print(prompt.replace(" ","")) # it deletes the spaces
print(question.replace(" ",""))