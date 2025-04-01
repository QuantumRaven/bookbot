#!/usr/bin/env python3


def count_words(text):
    return f"{len(text.split())}"


def char_count(num_text):
    conversion = num_text.lower()
    character_counts = {}
    for char in conversion:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts


def sorted_list(sort):
    if not sort:
        return []
    result = [{"character": char, "count": count} for char, count in sort.items()]
    sorted_result = sorted(result, key=lambda x: x["count"], reverse=True)
    return sorted_result
