def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def word_count(book):
    words = book.split()
    num_words = len(words)
    return f"Found {num_words} total words"


def char_dict_count(text):
    char_dict = {}
    # Add letters with corresponding counts to empty char_dict
    for letter in text.lower():
        if letter.isalpha():
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    return char_dict
    

def sorted_dict_list(char_dict):
    dict_list = []

    # Populate the list with dictionaries
    for key, val in char_dict.items():
        dict_list.append({key: val})

    # Sort the list by dictionary values
    sorted_list = sorted(dict_list, key=lambda d: list(d.values())[0], reverse=True)
    return sorted_list
