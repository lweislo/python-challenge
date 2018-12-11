#This script examines the word, sentence, and character counts in a body of text

import re
import os

file_path = os.path.join("raw_data", "paragraph_1.txt")

with open(file_path, 'r') as f:
    text = f.read()
    #Split the text on ending punctuation or line break
    sentences = re.split('[.?!]|[ \"]\n+', text)
    #Length of resulting list is approx. number of sentences
    no_sentences = len(sentences)
    
    tot_words = 0
    tot_letters = 0
    #Split the sentences on space to create list of words in list of sentences
    words = [s.split(' ') for s in sentences]
    for w in words:
        tot_words += len(w)
        for l in w:
            tot_letters += len(l)

print("Paragraph Analysis\n-----------------\n")
    print(f"Approximate Word Count: {tot_words}")
    print(f"Approximate Sentence Count: {len(sentences)}")
    print(f"Average Letter Count: {format(tot_letters/tot_words, '.2f')}")
    print(f"Average Sentence Length: {format(tot_words/len(sentences), '.2f')}")


