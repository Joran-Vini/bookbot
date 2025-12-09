from stats import get_book_words, get_unique_letters

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
        return content


def main():
    filepath = "books/frankenstein.txt"
    book_content = get_book_text(filepath)
    num_words = get_book_words(book_content)
    print(f"Found {num_words} total words")
    print("Unique words:")
    unique_letters = get_unique_letters(book_content)
    for letter, count in unique_letters.items():
        print(f"'{letter}': {count}")

if __name__ == "__main__":
    main()
