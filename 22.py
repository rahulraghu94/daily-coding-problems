"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible
reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
['bedbath', 'and', 'beyond'].


"""


word_set = ['quick', 'brown', 'the', 'fox']
string = "thequickbrownfox"


def if_word(str):
    return str if str in word_set else False


beginning = 0
result = []
for end in range(0, (len(string) + 1)):
    word = if_word(string[beginning:end])
    if word:
        result.append(word)
        beginning = end

print(result)

