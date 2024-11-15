'''Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"'''



def spin_words(sentence):
    
    MAX_LENGHT = 5
    
    final_sentence = []
    for word in sentence.split():
        if len(word) >= MAX_LENGHT:
            final_sentence.append(word[::-1])
        else:
            final_sentence.append(word)
    
    return ' '.join(final_sentence)