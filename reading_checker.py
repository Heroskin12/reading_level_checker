# Step 1 - Prompt user for input.
text = input("Text: ")
length = len(text)
txtup = text.upper()

# Step 2 - Declare and Initialise Variables
sentences = 0
letters = 0
words = 1

# Step 3 - Count Sentences
for c in txtup:
    if c == "?" or c == "!" or c ==".":
        sentences+= 1
    elif c.isalpha():
        letters+= 1
    elif c == " " or c == "\n":
        words+= 1

# print(f"{sentences}")
# print(f"{letters}")
# print(f"{words}")

# Step 4 - Complete math for formula.
# 4.1 = L, the average number of letters per 100 words.
L = (letters / words) * 100
# print(f"{L}")

# 4.2 - S, the average number of sentences per 100 words.
S = (sentences / words) * 100
# print(f"{S}")
# Step 5 - Calculate Luhn's Algorithm
CLI = round(0.0588 * L - 0.296 * S - 15.8)
# print(f"{CLI}")

# Step 6 - Determine reading age.
if CLI >= 1 and CLI <= 16:
    print(f"Grade {CLI}")
elif CLI < 1:
    print("Before Grade 1")
else:
    print("Grade 16+")