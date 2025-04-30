from HelperFunctions import get_sentences, remove_quotation

'''
Conditions Based on sample input

Ignore text similar to tags: <//g>
    Regex? 
    comparision of requirements: 1 "<", 1 optional "/", 1 Letter, 1 ">"

Correctly tagged Paragraph
    1. if tags are closed properly:

Expected A found B
    1. if A is closed by B
        mismatched tags

Expected # found </B>
    1. if tags close properly before a </B>
        tags close until </B>

Expected </B> found #
    1. if a <B> tag is left 
        <B> is never closed

'''

if __name__ == "__main__":


    sentences = get_sentences("Paragraph.txt")

    #stack 1 for <\w>
    stack_opening_tag = []
    #stack 2 for <\/\w>
    stack_closing_tag = []

    for sentence in sentences:
        words = sentence.split(" ")
        pass

'''
PSEUDO CODE

for each sentence in paragraph
    
    split sentence into words with delimeter " "
    for each word in sentence
        #used https://regex101.com/ for testing
        If word matches <\w> : eg <A>
            add to stack 1
        If word matches <\/\w> : eg </A>
            add to stack 2

    for length of smallest stack
        A = stack1.pop
        B = stack2.pop

        if A != remove_slash(B)
            output, Expected add_slash(A) found B 
            break
    if stack1 is not empty
        output, expected add_slash(stack1.pop) found #

    elif stack2 is not empty
        output, expected # found stack2.pop
    
    else
        output, Correctly tagged paragraph
        
'''