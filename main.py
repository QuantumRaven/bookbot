#!/usr/bin/env python3

from stats import count_words, char_count, sorted_list
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    character_counts = char_count(book_text)
    sorted_counts = sorted_list(character_counts)

    # Your reporting code would go here
    # Make sure to uncomment the print statements you need

    # For the test requirements, you need at least:
    print(f"Found {word_count} total words")
    for item in sorted_counts:
        if item["character"] == "e" or item["character"] == "t":
            print(f"{item['character']}: {item['count']}")


main()
