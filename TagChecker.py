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

'''
PSEUDO CODE

read from paragraph
split paragraph with delimeter "," into sentences
for each sentence in paragraph
    
    split sentence into words with delimeter " "
    for each word in sentence
        #used https://regex101.com/ for testing
        If word matches <\w> : eg <A>
            add to stack
        If word matches <\/\w> : eg </A>
            if stack[-1] == remove_slash(word)
                stack.pop
            else
                output expected A found B
                skip sentence = Return?


    if stack is empty
        output Correctly tagged paragraph
    if stack has <A> 
        output expected </A> found #
    
'''