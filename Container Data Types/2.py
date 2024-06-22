def word_counter(sentence):
    # Convert the sentence to lowercase to ignore case sensitivity
    sentence = sentence.lower()
    
    # Remove punctuation marks except for apostrophes (to handle contractions properly)
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    sentence = ''.join([char for char in sentence if char not in punctuation])
    
    # Split the sentence into words
    words = sentence.split()
    
    # Dictionary to store word counts
    word_count = {}
    
    # Count occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Print the word counts in the specified format
    print("{", end="")
    for word, count in word_count.items():
        print(f"{word}:{count},", end=" ")
    print("}")

# Example usage:
if __name__ == "__main__":
    # Input a sentence
    sentence = input("Enter a sentence: ")
    
    # Call the function to count words and print in the specified format
    word_counter(sentence)
