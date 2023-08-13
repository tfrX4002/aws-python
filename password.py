word = "ExercisePython"
word_alternant = " "
for i, letter in enumerate(word):
    if i % 2 == 0:
        word_alternant += letter.upper()
    else:
        word_alternant += letter.lower()
print(word_alternant)


