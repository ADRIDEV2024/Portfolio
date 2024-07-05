"""
Create a program that analizes text and get :

- Total number of words
- Longer word
- Total number of sentences in that text
- Average word length
"""

import re
from typing import List, Tuple


def count_words(words: List[str]) -> int:
    return len([word for word in words if word])

def count_letters(words: List[str]) -> int:
    return sum(len(re.sub(r"[^\w]", "", word)) for word in words if word)

def count_sentences(words: List[str]) -> int:
    return sum(1 for word in words if "." in word)

def find_longest_words(words: List[str]) -> List[str]:
    longest_word = []
    for word in words:
        current_word = re.sub(r"[^\w]", "", word)
        if len(current_word) == 0:
            continue

        if len(longest_word) == 0 or len(longest_word[0]) == len(current_word):
            longest_word.append(current_word)
        elif len(current_word) > len(longest_word[0]):
            longest_word.clear()
            longest_word.append(current_word)
    return longest_word

def parse(text: str) -> Tuple[int, int, int, List[str]]:
    words = text.replace("\n", " ").split(" ")
    words_count = count_words(words)
    letter_count = count_letters(words)
    sentences_count = count_sentences(words)
    longest_word = find_longest_words(words)
    
    return words_count, letter_count, sentences_count, longest_word


    print(f"Total number of words is : {words_count}\n")
    print(f"The Average word length is: {letter_count // words_count}\n")
    print(f"Number of sentences: {sentences_count}\n")
    print(f"Longest word is: {longest_word}")
    
parse("This is a simple text for this practical exercise")

