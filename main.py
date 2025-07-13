import sys
from stats import get_num_words, get_char_count, char_sort


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return (file_contents)

def main(): 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path=sys.argv[1]
    contents=get_book_text(path)
    num_words=(get_num_words(contents))
    num_chars=(get_char_count(contents))
    sorted_chars=(char_sort(num_chars))

    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    
    for chars in sorted_chars:
        if chars["char"].isalpha():
            print(f"{chars['char']}: {chars['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
