

def reverse_string_by_words(phrase: str) -> str:
    new_phrase = ""
    word = ""
    for letter in list(phrase):
        if letter.isspace() or letter in "!\"\'(),./:;<=>?[]{}":
            new_phrase += "".join(reversed(word))
            word = ""
            new_phrase += letter
        else:
            word += letter
    if len(word):
        new_phrase += "".join(reversed(word))
    return new_phrase


if __name__ == "__main__":
    assert reverse_string_by_words("") == ""
    assert reverse_string_by_words("Hello world!") == "olleH dlrow!"
    assert reverse_string_by_words("Hello  olleH") == "olleH  Hello"

    input_phrase = input().strip()
    output_phrase = reverse_string_by_words(input_phrase)
    print(f"Input phrase : {input_phrase}")
    print(f"Output phrase : {output_phrase}")

