def get_num_words(book_contents):
    words = book_contents.split()
    num_words = len(words)
    return(num_words)

def get_char_count(book_contents):
    lower_case = book_contents.lower()
    char_count = {}
    for char in lower_case:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return(char_count)

def sort_on(char_count):
    return char_count["num"]

def char_sort(counted_chars):
    dict_list = []
    for key, value in counted_chars.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(key= sort_on, reverse= True)
    return(dict_list)
