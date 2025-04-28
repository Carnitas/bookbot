import sys

from stats import get_letter_count, get_num_words, sort_letter_count


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
    with open(sys.argv[1], encoding="utf-8") as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        letter_count = get_letter_count(file_contents)
        sorted_letter_count = sort_letter_count(letter_count)
    print(f"Found {num_words} total words")
    for count in sorted_letter_count:
        if count["char"].isalpha():
            print(f"{count['char']}: {count['num']}")


if __name__ == "__main__":
    main()
