'''
Functions used by TagChecker.py
'''

def get_sentences(file_path):

    f = open(file_path)
    paragraph = f.read()
    return paragraph.split(",")

def remove_quotation(text):
    #also removing new lines
    return text[1:-1].replace('"','').replace("\n","")
    