
def get_sentences(file_path):

    f = open(file_path)
    paragraph = f.read()
    return paragraph.split(",")

    