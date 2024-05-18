def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path=book_path, num_words=num_words, chars_dict=chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    chars_dict = dict(
        sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
    )
    for k, v in chars_dict.items():
        if not k.isalpha():
            continue
        print(f"The '{k}' character was found {v} times")
    return


main()
