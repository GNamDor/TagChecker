'''
Functions used by TagChecker.py
'''
import re


def get_sentences(file_path):
    '''
    get sentences from txt file, split sentences based on if they have " and , 
    '''
    f = open(file_path)
    paragraph = f.read()
    return paragraph.strip().split('",')

def preprocess_sentence(text):
    '''
    add padding for all the tags using replace method
    '''
    insert_space = text.replace(">","> ")
    result = insert_space.replace("<", " <")
    return result
    

def remove_slash(word):
    '''
    convert a closing tag to an open tag
    useful for printing the output string
    '''
    return word[0]+word[2:]    

def add_slash(word):
    '''
    convert an open tag to a closing tag
    useful for printing the output string
    '''
    return word[0] + "/" + word[1:]   

def regex_sort(words, op_stack):
    '''
    use regex to compare if a Tag has <, /, A-Z and >, if so, store them either in
    stack or queue
    '''

    for word in words:
        if re.match(r"<[A-Z]>", word):
            op_stack.append(word)
        elif re.match(r"<\/[A-Z]>", word):
            # try to access last item
            if len(op_stack)<1:
                return f'"Expected # found {word}",'
            # if tags match pop them
            if op_stack[-1] == remove_slash(word):
                op_stack.pop()
            else:
                return f'"Expected {add_slash(op_stack.pop())} found {word}",'

    if len(op_stack)>0:
        return f'"Expected {add_slash(op_stack.pop())} found #",'
    return 'Correctly tagged paragraph",'
