#a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
a=input(' enter the fruits name: ')
words=[word for word in a.split(",")]
print(",".join(sorted(list(set(words)))))