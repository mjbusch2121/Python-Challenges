def reverse_sentence(sentence):
    # Split the sentence into a list of words (splits by spaces)
    # "Hello World" becomes ['Hello', 'World']
    words = sentence.split()

    # Reverse the order of words, then join them back with spaces
    # reversed(['Hello', 'World']) creates ['World', 'Hello']
    # " ".join() puts them back together with spaces: "World Hello"
    reversed_sentence = " ".join(reversed(words))

    # Return the reversed sentence
    return reversed_sentence

# Test the function
# Expected output: "World Hello"
print(reverse_sentence("Hello World"))