from stats import get_book_words, get_unique_letters, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
        return content


def main():
    if (sys.argv.__len__() < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    filepath = sys.argv[1]
    print(f"Analyzing book found at {filepath}...")
    book_content = get_book_text(filepath)
    num_words = get_book_words(book_content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    unique_letters = get_unique_letters(book_content)
    sorted_letters = sort_dictionary(unique_letters)
    for item in sorted_letters:
        print(f"{item['char']}: {item['num']}")

    print("============ THE END ============")

if __name__ == "__main__":
    main()
