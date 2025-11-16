def word_count(text):
    words = text.split()
    return len(words)

def unique_letter_count(text):
    text = text.lower()
    unique_char = {}

    for char in text:
        if char.isalpha():
            if char in unique_char:
                unique_char[char] += 1
            else:
                unique_char[char] = 1
    unique_char = [{"char": char, "num": count} for char, count in unique_char.items()]
    return unique_char

def sort_on(item):
    return item["num"]