# Write a function that removes repeated characters from a string.
# Sample strings are: a Hello: Output should be Helo b. Concatenate: output should be Conaten


def duplicate_letters(p):
    q = ''
    for char in p:
        if char not in q.casefold():
         q += char

    print(q)
duplicate_letters('Concatenate')
duplicate_letters('Hello')

