from collections import Counter

word_counter = Counter()
with open("data.txt", "r") as file:
    for line in file:
        words = line.lower().replace(',','').replace(',','').split()
        word_counter.update(words)

most_common_words = word_counter.most_common(10)
print("Most frequent words: ")
for word, count in most_common_words:
    print(f"{word}: {count}")