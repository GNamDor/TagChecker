'''
Functions used by TagChecker.py
'''

def get_sentences(file_path):

    f = open(file_path)
    paragraph = f.read()
    return paragraph.split(",")

def remove_quotation(text):
    if text[0] == '"' and text[-1] == '"':
        return text[1:-1]
    