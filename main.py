def main():
    frankenstein_path = "books/frankenstein.txt"
    text = load_contents(frankenstein_path)
    num_words = count_contents(text)
    chars_dict = cont_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {frankenstein_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def load_contents(path):
    with open(path) as f:
        return f.read()

def count_contents(text):
    words = text.split()
    return len(words)

def cont_characters(text):
    char_count = {}
    words = text.lower()

    for char in words:
        if char in char_count:
            # if character exists, increment its count
            char_count[char] += 1
        else:
            # if character doesn't exist, set its count to 1
            char_count[char] = 1

    return char_count

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()