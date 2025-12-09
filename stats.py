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
            if not letter.isalpha():
                continue
            letter = letter.lower()
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    return dictionary

def sort_dictionary(dictionary):
    list = []
    for key, value in dictionary.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        list.append(new_dict)
        list.sort(key=sort_on, reverse=True)
    return list

def sort_on(item):
    return item["num"]           