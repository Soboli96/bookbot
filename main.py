import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

from stats import get_num_words
from stats import get_character_count
from stats import char_sort


with open(book_path) as file:
    text = file.read()
word_count = get_num_words(text)
#char_count = get_character_count(text)
sorted_counts = char_sort(text)

print(f"Found {word_count} total words")
#print(char_count)
for char, count in sorted_counts:
    print(f"{char}: {count}")