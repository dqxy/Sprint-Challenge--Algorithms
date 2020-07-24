'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    # If the input length is less than or equal to one, then return the counter
    if len(word) <= 1:
        return count

    # Verify first two positions for th occurence
    if word[0:2] == 'th':
        # If occurence is found, increment th counter
        count += 1

    # Continue recursion and verify all occurences are counted to the end
    return count + count_th(word[1:])

print(count_th("aththth"))
