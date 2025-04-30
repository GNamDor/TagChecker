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

