def get_num_words(text):
    num_words = len(text.split())
    return num_words




def get_character_count(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
    

def char_sort(text):
    char_counts = get_character_count(text)
    sorted_counts = sorted(
        [(char, count) for char, count in char_counts.items() if char.isalpha()],
        key=lambda x: x[1],
        reverse=True
    )
    return sorted_counts