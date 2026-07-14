def count_long_words(*words):
    count = 0

    for word in words:
        if len(word) > 4:
            count += 1

    return count

print(count_long_words("cat", "kitten", "dog", "engineer"))  # 2
print(count_long_words("me", "you")) 