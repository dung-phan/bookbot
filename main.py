from stats import get_num_words, char_count, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(counts, num_words, book_path):
    report = ''
    for count in counts:
        report += f"{count['char']}: {count['num']}\n"

    print(f"""
        ============ BOOKBOT ============
        Analyzing book found at {book_path}...
        ----------- Word Count ---------
        Found {num_words} total words
        --------- Character Count -------
        {report}
        ============= END ===============
        """)
def main():
    args = sys.argv
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = args[1]
        book_text = get_book_text(book_path)
        num_words = get_num_words(book_text)
        char_dict = char_count(book_text)
        print_report(sort_dict(char_dict), num_words, book_path)

main()
