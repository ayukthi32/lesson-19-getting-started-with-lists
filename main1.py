#activity2
def match_words(words):
    ctr = 0
    lst =[]
    for word in words:
        if len(word) > 1 and word[0] == word [-1]:
            ctr += 1
            lst.append(word)
    print("List of words with first and last letter same" , lst)
    return ctr
count = match_words(["abc" , "bgb" , "1234" , "987"])
print("Number of words having the same first and last letter are" , count)
