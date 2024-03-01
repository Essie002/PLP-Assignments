word_list = ["apple", "banana", "orange", "kiwi", "pear", "grape"]

odd_words = []  # Initialize an empty list to store odd-length words

for word in word_list:
    if (len(word) % 2) != 0:
        odd_words.append(word)  # Append odd-length words to the list

print(odd_words)  # Print the list of odd-length words after the loop


    
