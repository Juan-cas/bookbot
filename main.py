from stats import get_word_numbers
from stats import get_book_text
from stats import get_number_characters
from stats import organize_dictionary
from stats import information_printer
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    word_numbers = get_word_numbers(book)
    letter_numbers = get_number_characters(book)
    organized_dictionary = organize_dictionary(letter_numbers)
    information_printer(book_path, word_numbers, organized_dictionary)

if __name__ == "__main__":
    main()
