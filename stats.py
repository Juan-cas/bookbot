import string

def get_book_text(path_to_file):
    word = []
    word_numbers = 0
    with open(path_to_file, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content

def get_word_numbers(file_content):
    words = file_content.split()
    word_numbers = 0
    for word in words:
        word_numbers += 1
    return word_numbers

def get_number_characters(file_content):
    letter_count = {letter:0 for letter in string.ascii_lowercase}
    lower_content = file_content.lower()
    for letter in lower_content:
        if letter in letter_count:
            letter_count[letter] += 1
    return letter_count

def organize_dictionary(numbered_letters):
        list_of_dictionaries = list(numbered_letters.items())
        return list_of_dictionaries

def information_printer(book_path, word_count, character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for index in character_count:
        print(index[0] + ":", index[1])
    print("============= END ===============")
