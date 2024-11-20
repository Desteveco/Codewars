def duplicate_encode(word):
    word_lowercase = word.lower()
    
    return "".join([")" if word_lowercase.count(letter) > 1 else "(" for letter in word_lowercase])