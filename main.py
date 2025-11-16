from stats import word_count, unique_letter_count, sort_on
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    
    book_text = get_book_text(book_path)
    count = word_count(book_text)
    print(f"Found {count} total words")
    
    print("--------- Character Count -------")
    
    unique_count = unique_letter_count(book_text)
    unique_count.sort(reverse=True, key=sort_on)  # Highest to lowest
    
    # Print each character and its count
    for item in unique_count:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")