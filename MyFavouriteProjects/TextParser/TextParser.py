"""
Create a program that analizes text and get :

- Total number of words
- Longer word
- Total number of sentences in that text
- Average word length

"""

import re



def parse(text: str) -> str:

    words_count = 0
    letter_count = 0
    sentences_count = 0
    longest_word = []

    words = text.replace("\n", " ").split(" ")

    for word in words:

        if len(word) != 0:

            if "." in word:
                sentences_count += 1

            current_word = re.sub(r"[^\w]", "", word)

            print(current_word)

            words_count += 1
            letter_count += len(current_word)

            if len(longest_word) == 0 or len(longest_word[0]) == len(current_word):
                longest_word.append(current_word)
            elif len(current_word) > len(longest_word[0]):
                longest_word.clear()
                longest_word.append(current_word)

    print(f"Total number of words is : {words_count}\n")
    print(f"The Average word length is: {letter_count // words_count}\n")
    print(f"Number of sentences: {sentences_count}\n")
    print(f"Longest word is: {longest_word}\n")
    

parse("This is a simple text for this practical exercise")
