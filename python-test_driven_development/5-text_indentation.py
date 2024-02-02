#!/usr/bin/python3
"""
write a function that prints a text with 2 new lines
after each of the characters: '.', '?' and ':'
"""
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Parameters:
      text (str): The input text.

    Raises:
      TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # chars_to_new_line = ['.', '?', ':']
    # current_line = ""

    # for char in text:
    #     current_line += char
    #     if char in chars_to_new_line:
    #         print(current_line.strip())
    #         print()
    #         current_line = ""

    # if current_line:
    #     print(current_line.strip())

    start_index = 0

    for i in range(len(text)):
        if text[i] in (".", "?", ":"):
            print(text[start_index: i + 1].strip(), end="\n\n")
            start_index = i + 1
    print(text[start_index: len(text)].strip(), end="")
    