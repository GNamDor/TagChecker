'''
Test.py is only for testing the functions imported from HelperFunctions.py
HelperFunctions.py will be exposing its functions for TagChecker.py
'''

from HelperFunctions import *

sentences = get_sentences("Paragraph.txt")

# print(sentences)
# print(remove_quotation(sentences[0]))

word = "</B>"
stack1 = []
stack2 = []

regex_comparison(word, stack1, stack2)

print("stack1 ",stack1)
print("stack2 ",stack2)