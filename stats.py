def get_num_words(text):
    return len(text.split())

def char_count(text):
    char_dict = {}
    for word in text.lower().split():
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(d):
    return d['num']

def sort_dict(counts_dict):
    new_list = []

    for count in counts_dict:
        if count.isalpha():
            new_list.append({
                "char": count,
                "num": counts_dict[count]
            })
    new_list.sort(key=sort_on, reverse=True)

    return new_list



