'''
Functions used by TagChecker.py
'''
import re

def get_sentences(file_path):

    f = open(file_path)
    paragraph = f.read()
    return paragraph.split('",')

def preprocess_sentence(text):
    
    #add padding for > and < 
    insert_space = text.replace(">","> ")
    result = insert_space.replace("<", " <")
    return result
    
def regex_sort(word, op_stack, cl_stack):
    if re.match("<[A-Z]>", word):
        op_stack.append(word)
    elif re.match("<\/[A-Z]>", word):
        cl_stack.append(word)
    