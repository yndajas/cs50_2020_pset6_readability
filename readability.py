from cs50 import get_string

text = get_string("Text: ")

# initialise counr variables
letters = 0
words = 0
sentences = 0

# loop through all chraracters of text
for i in range(len(text)):
    # get unicode/ASCII decimal value of character
    char_dec = ord(text[i])

    # if A:Z or a:z
    if (char_dec >= 65 and char_dec <= 90) or (char_dec >= 97 and char_dec <= 122):
        letters += 1
    # if space
    elif char_dec == 32:
        words += 1
    # if . ! ?
    elif char_dec == 46 or char_dec == 33 or char_dec == 63:
        sentences += 1

# as word count is only incremented by spaces, the final word needs adding (if there are any words)
if words > 0:
    words += 1

# get average number of letters per 100 words
l = float(letters) / float(words) * 100

# get average number of sentences per 100 words
s = float(sentences) / float(words) * 100

# calculate Coleman-Liau index, round it and assign the result to variable grade
grade = round(0.0588 * l - 0.296 * s - 15.8)

# print grade
if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")