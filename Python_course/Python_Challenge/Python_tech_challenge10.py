# Create a function that converts any string value to a sentence case.
# The write a unit test that checks the functions correctness



def sentence_case(string):
    word = string.capitalize()
    print(word)
    return word

sentence_case('the boy is walking')