n = int(input())

words = []
for i in range(n):
    words.append(input())

words = set(words)
sorted_words = sorted(words, key=lambda x: (len(x), x))

for i in range(len(sorted_words)):
    print(sorted_words[i])