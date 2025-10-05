def get_num_words(book: str) -> int:
    return len(book.split())


def get_letter_count(book: str) -> dict[str, int]:
    letter_dict: dict[str, int] = {}
    for word in book:
        for letter in word.lower():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict


def sort_letter_count(counts: dict[str, int]) -> list[dict[str, str | int]]:
    word_counts: list[dict[str, int | str]] = [{"char": char, "num": num} for char, num in counts.items()]
    return sorted(word_counts, key=lambda k: k["num"], reverse=True)
