def join_words(*words):
    result = ""
    for word in words:
        result += word + " "

    return result[:-1]

print(join_words("I", "am", "learning", "Python"))
print(join_words("hello"))