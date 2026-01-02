import sys
from stats import get_book_text, word_count, char_dict_count, sorted_dict_list


def main():
    # Validate sys arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        # Pull in variables
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        char_list = sorted_dict_list(char_dict_count(text))

        # Generate report section 1
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"{word_count(text)} total words")
        print("--------- Character Count -------")
        
        # Generate report section 2
        for char in char_list:
            for key, val in char.items():
                print(f"{key}: {val}")


if __name__ == "__main__":
    main()