def print_upper_words(words, must_start_with=None):
    """
    Print each word from a list in uppercase.
    Optionally, only print words that start with certain letters.

    - words: list of words
    - must_start_with: a set of letters; if provided, only words starting with these letters are printed
    """
    for word in words:
        if must_start_with is None or word[0].lower() in must_start_with:
            print(word.upper())

# Testing the function
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
