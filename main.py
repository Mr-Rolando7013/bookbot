from stats import count_words, sortDict
import sys

def get_book_text(bookFile):
    with open(bookFile) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookFile = sys.argv[1]

    text = get_book_text(bookFile)
    wordCount = 0
    dictCount, wordCount = count_words(text)
    #print(dictCount)
    sortDict(dictCount, wordCount)

if __name__ == "__main__":
    main()
