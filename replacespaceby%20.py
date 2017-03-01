def replacespace(sentence):
    ans_string = ""
    for each in sentence:
        if each == " ":
            ans_string += "%20"
        else:
            ans_string += each
    return ans_string
print (replacespace("The world is a difficult place to survive"))
#Output is "The%20world%20is%20a%20difficult%20place%20to%20survive""
