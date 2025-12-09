def get_book_text(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
        return content

def get_book_words(book):
    num_words = 0
    book_split = book.split()
    for word in book_split:
        num_words += 1
    return num_words

def main():
    filepath = "books/frankenstein.txt"
    book_content = get_book_text(filepath)
    num_words = get_book_words(book_content)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()
