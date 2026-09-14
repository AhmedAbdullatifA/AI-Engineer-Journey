def count_words(text: str):
    words = text.split()
    return len(words)

text = "This is a test string"
print(count_words(text))  # Output: 5