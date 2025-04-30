'''
Functions used by TagChecker.py
'''

def get_sentences(file_path):

    f = open(file_path)
    paragraph = f.read()
    return paragraph.split('",')

def preprocess_sentence(text):
    
    #add padding for > and < 
    insert_space = text.replace(">","> ")
    result = insert_space.replace("<", " <")
    return result
    