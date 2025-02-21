import sys

from stats import get_num_words
from stats import get_char_count
from stats import sorted_char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # path_to_file = "books/frankenstein.txt"
    path_to_file = sys.argv[1]

    file_contents = get_book_text(path_to_file)

    components = []
    components.append("============ BOOKBOT ============")
    components.append(f"Analyzing book found at {path_to_file}...")
    components.append(f"----------- Word Count ----------")
    components.append(f"Found {get_num_words(file_contents)} total words")
    components.append(f"----------- Character Count ----------")
    
    char_count_dictionary = get_char_count(file_contents)
    for item in sorted_char_count(char_count_dictionary):
        key = list(item.keys())[0]
        if key.isalpha():
            components.append(f"{key}: {item[key]}")
    components.append("============ END ============")
    print("\n".join(components))
    
def get_report(dictionary):
    components = []
    
    return components

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()