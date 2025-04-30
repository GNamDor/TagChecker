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
    
def regex_sort(word, op_stack, cl_queue):
    if re.match("<[A-Z]>", word):
        op_stack.append(word)
    elif re.match("<\/[A-Z]>", word):
        cl_queue.append(word)

def remove_slash(word):
    return word[0]+word[2:]    

def add_slash(word):
    return word[0] + "/" + word[1:]   

def output_processing(smallest_stack_size, stack_op_tag, queue_cl_tag):
    
    for _ in range(smallest_stack_size):
        op = stack_op_tag.pop()
        cl = queue_cl_tag.popleft()
        
        if op != remove_slash(cl):
            return f"Expected {add_slash(op)} found {cl}"
            
    if len(stack_op_tag) > 0:
        return f"Expected {add_slash(queue_cl_tag.pop())} found #"
    elif len(queue_cl_tag) > 0:
        return f"Expected # found {queue_cl_tag.pop()}"
    else:
        return "Correctly tagged paragraph"