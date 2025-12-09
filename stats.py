def get_book_words(book):
    num_words = 0
    book_split = book.split()
    for word in book_split:
        num_words += 1
    return num_words

def get_unique_letters(book):
    dictionary = {}
    book_split = book.split()
    for word in book_split:
        for letter in word:
            letter = letter.lower()
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    return dictionary
