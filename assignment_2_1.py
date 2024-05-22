def palindrome(my_string, start, end):
    """
    Decides if a part of text is palindrome and returns corresponding boolean value.
    :param str my_string: text to be analyzed
    :param int start: index of start of palindrome in the text
    :param int end: index of the end of palindrome in the text
    :rtype: bool
    :return: True if selected part of text is palindrome
    """
    # Vyber podretezec, ktery budes analyzovat
    my_string = my_string[start:end]

    # Odstran mezery v retezci
    my_string = my_string.replace(" ", "")

    # Preved retezec na mala pismena
    my_string = my_string.lower()

    # Odstran interpunkci na konci retezce
    my_string = my_string.rstrip(".?!:,")

    # Najdi index prostredni prvku retezce (pozor na retezce se sudym poctem znaku)
    middle_idx = int(len(my_string)/2 + len(my_string) % 2)- 1

    # Rozdel retezce na poloviny (dva podretezce)
    left_substring = my_string[:middle_idx+1 - len(my_string)%2]
    right_substring =my_string[middle_idx + 1 :]


    # Rozhodni, jestli se jedna o palindrom
    is_palindrome = left_substring == right_substring[::-1]

    return is_palindrome


if __name__ == "__main__":
    test_string = "krkavec"
    palindrome_start = 0
    palindrome_end = 2

    is_string_palindrome = palindrome(test_string, palindrome_start, palindrome_end)
