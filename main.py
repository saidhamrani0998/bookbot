from typing import Dict
from collections import defaultdict


def count_words(text: str) -> Dict:
    count = defaultdict(int)
    for char in text:
        if char.isalpha():
            count[char.lower()] += 1
    return count


def sort_dict(dictionnary: Dict) -> Dict:
    sorted_dict = sorted(dictionnary.items(), reverse=True, key=lambda x: x[1])
    return dict(sorted_dict)


def main():
    with open('books/frankenstein.txt') as file:
        content = file.read()
        word_count = sort_dict(count_words(content))
        print(f"*-The text has {len(content.split())} words-*")
        for item in word_count:
            print(
                f"*--the character {item} has appeared {word_count[item]} times--*")


if __name__ == "__main__":
    main()
