def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)  # Print the first 1000 characters of the book text