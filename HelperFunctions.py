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
    
def regex_comparison(word, stack_op_tag, stack_cl_tag):
    if re.match("<[A-Z]>", word):
        stack_op_tag.append(word)
    elif re.match("<\/[A-Z]>", word):
        stack_cl_tag.append(word)
    