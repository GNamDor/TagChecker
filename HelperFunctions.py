'''
Functions used by TagChecker.py
'''

def get_sentences(file_path):

    f = open(file_path)
    paragraph = f.read()
    return paragraph.split(",")

def preprocess_sentence(text):
    #also removing new lines
    removed_quotations = text[1:-1].replace('"','')
    removed_newline = removed_quotations.replace("\n","\n")
    #add padding for > and < 
    insert_space = removed_newline.replace(">","> ")
    result = insert_space.replace("<", " <")
    return result
    