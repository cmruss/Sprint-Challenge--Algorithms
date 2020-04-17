'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # the sequence to evaluate
    string = 'th'
    # word defined as str, was calling as int?
    word = str(word)
    # TBC
    # if the word is shorter than the string return 0
    if len(word) == 0 or len(word) < len(string):
        return 0
    # if the current index in the word sliced to the length of the string
    # is equal to 'th' return the function fro the next index + 1
    if (word[0:len(string)] == string):
        return count_th(word[len(string)-1:]) +1
    else:
        # return the function for the next index to evaluate
        return count_th(word[len(string)-1:])
