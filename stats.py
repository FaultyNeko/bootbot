def word_count(text):
    words = text.split()
    return len(words)

def unique_letter_count(text):
    text = text.lower()
    unique_char = {}

    for char in text:
        if char in unique_char:
            unique_char[char] += 1
        else:
            unique_char[char] = 1
    return unique_char