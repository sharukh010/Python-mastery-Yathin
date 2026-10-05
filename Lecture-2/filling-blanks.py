word = "banana"
# index function will always return the first occurence position
# print(word.index("b"))
start = -1 
count = word.count("a")
while count > 0: 
    # print(count)
    start = word.index("a",start+1)
    print(start)
    count -= 1 