from stats import word_count, unique_letter_count

def get_book_text(path):
    with open(path) as f:
        return f.read()



if __name__ == "__main__":
    book_text = get_book_text("books/frankenstein.txt")
    count = word_count(book_text)
    print(f"Found {count} total words")
    unique_count = unique_letter_count(book_text)
    print(f"Found {unique_count} unique letters")