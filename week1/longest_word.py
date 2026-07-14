def longest_word(*words):
    champion = words[0]

    for word in words:
        if len(word) > len(champion):
            champion = word

    return champion

print(longest_word("cat", "dog", "kitten"))
print(longest_word("me", "you"))
print(longest_word("engineer"))