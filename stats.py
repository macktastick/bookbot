def get_num_words(string):
    return len(string.split())

def get_char_count(string):
    count = {}
    for char in string:
        nchar = char.lower()
        if nchar in count:
            count[nchar] += 1
        else:
            count[nchar] = 1
    return count

def sort_on(dict):
    k = list(dict.keys())[0]
    return dict[k]

def sorted_char_count(char_count):
    char_counts = []
    for char in char_count:
        dictionary = {}
        dictionary[char] = char_count[char]
        char_counts.append(dictionary)
    char_counts.sort(reverse=True, key=sort_on)
    return char_counts

